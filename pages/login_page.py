from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID,"username")
    PASSWORD_FIELD = (By.ID,"password")
    SUBMIT_BUTTON = (By.XPATH,"//button[@type = 'submit']")
    URL = "https://the-internet.herokuapp.com/login"
    FLASH_MESSAGE = (By.ID, "flash")

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self,username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)

    def enter_password(self,password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def get_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.FLASH_MESSAGE))
        return message.text

    def login(self,username,password):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    

    

