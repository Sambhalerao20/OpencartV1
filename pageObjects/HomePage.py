from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    lnk_myaccount_xpath = "//span[text()='My Account']"
    lnk_register_xpath = "//a[text()='Register']"
    lnk_login_xpath = "//a[text()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_myaccount_xpath))
        )
        element.click()

    def clickRegister(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_register_xpath))
        )
        element.click()

    def clickLogin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_login_xpath)))
        element.click()


