from selenium.webdriver.common.by import By

class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_telephone_name = "telephone"
    txt_password_name = "password"
    txt_confirmpwd_name = "confirm"
    txt_privacypolicy_name = "agree"
    btn_continue_xpath = "//input[@value='Continue']"
    txt_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setTelephone(self, telephone):
        self.driver.find_element(By.NAME, self.txt_telephone_name).send_keys(telephone)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def setConfPassword(self, confpassword):
        self.driver.find_element(By.NAME, self.txt_confirmpwd_name).send_keys(confpassword)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.txt_privacypolicy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_msg_conf_xpath).text
        except:
            return None