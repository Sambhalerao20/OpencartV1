import pytest
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

@pytest.mark.regression
class Test_001_AccountReg:
    baseURL= Readconfig.getApplicationURL()
    logger=LogGen.loggen()    # For logging

    def test_account_reg(self,setup):
        self.logger.info("*** test_001_AccountRegistration started ***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("Providing customer details for the registartion")
        self.regpage=AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Doe")
        self.email=randomString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone(9898989898)
        self.regpage.setPassword("Sam@14317")
        self.regpage.setConfPassword("Sam@14317")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getConfirmationMsg()
        # self.driver.close()

        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("Registartion is passed")
            assert True
        else:
            self.logger.info("Registartion is failed")
            assert False

        self.logger.info("*** test_001_AccountRegistration finished ***")


#  pytest -v -s testCases/test_001_AccountReg.py (All browser)
# pytest -v -s .\testCases\test_001_AccountReg.py --browser=edge
# pytest -v -s .\testCases\test_001_AccountReg.py --browser=chrome
# pytest -v -s .\testCases\test_001_AccountReg.py --browser=firefox

## Grouping testing: pytest -v -s testCases/ -m "sanity" --browser=chrome