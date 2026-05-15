import time
import os
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_Login_DDT:

    baseURL = Readconfig.getApplicationURL()
    logger = LogGen.loggen()

    path = os.path.abspath(os.curdir) + "\\testdata\\Opencart_LoginData.xlsx"

    def test_login_ddt(self, setup):

        self.logger.info("******** Starting DDT Login Test ********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

        lst_status = []

        for r in range(2, self.rows + 1):

            self.logger.info(f"******** Login DDT Iteration : {r} ********")

            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(2)

            self.targetpage = self.lp.isMyAccountPageExists()

            # Valid Data
            if self.exp == 'Valid':

                if self.targetpage == True:

                    self.logger.info("****** Passed ******")
                    lst_status.append("Pass")
                    self.ma.clickLogout()

                else:

                    self.logger.info("****** Failed ******")
                    lst_status.append("Fail")

            # Invalid Data
            elif self.exp == 'Invalid':

                if self.targetpage == True:

                    self.logger.info("****** Failed ******")
                    lst_status.append("Fail")
                    self.ma.clickLogout()

                else:

                    self.logger.info("****** Passed ******")
                    lst_status.append("Pass")

        self.driver.quit()

        # Final Assertion
        if "Fail" not in lst_status:

            self.logger.info("******** DDT Login Test Passed ********")
            assert True

        else:

            self.logger.error("******** DDT Login Test Failed ********")
            assert False, "DDT Login Test Failed"

        self.logger.info("******** End of DDT Login Test ********")


# pytest -v -s testCases/test_003_login_ddt.py (All browser)
# pytest -v -s .\testCases\test_003_login_ddt.py --browser=edge
# pytest -v -s .\testCases\test_003_login_ddt.py --browser=chrome
# pytest -v -s .\testCases\test_003_login_ddt.py --browser=firefox
# pytest -v -s testCases --browser=edge  > To execute test cases under 'testCases' module