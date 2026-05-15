import os
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities import randomString
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

@pytest.mark.sanity
class Test_002_Login():
    baseURL= Readconfig.getApplicationURL()
    logger=LogGen.loggen()    # For logging

    user = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("*** test_002_Login started ***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage = self.lp.isMyAccountPageExists()
        if self.targetpage == True:
            assert True

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshot"+"test_002_Login.png")
            assert False

        self.driver.close()
        self.logger.info("*** test_002_Login finished ***")

# pytest -v -s testCases/test_002_Login.py (All browser)
# pytest -v -s .\testCases\test_002_Login.py --browser=edge
# pytest -v -s .\testCases\test_002_Login.py --browser=chrome
# pytest -v -s .\testCases\test_002_Login.py --browser=firefox
# pytest -v -s testCases --browser=edge  > To execute test cases under 'testCases' module

## Grouping testing: pytest -v -s testCases/ -m "sanity" --browser=chrome