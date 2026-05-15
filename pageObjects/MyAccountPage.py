from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAccountPage:

    lnk_myaccount_xpath = "//span[normalize-space()='My Account']"
    lnk_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):

        # Click My Account dropdown first
        myaccount = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.lnk_myaccount_xpath)
            )
        )

        myaccount.click()

        # Then click Logout
        logout = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.lnk_logout_xpath)
            )
        )

        logout.click()