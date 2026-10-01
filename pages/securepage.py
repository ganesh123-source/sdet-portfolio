from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class SecurePage(BasePage):
    HEADING = (By.TAG_NAME,"h2")
    LOGOUT_BTN = (By.XPATH,"//a[@href = '/logout']")

    def get_heading(self):
        heading = self.wait.until(EC.visibility_of_element_located(self.HEADING))
        return heading.text

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()

    def get_url(self):
        return self.driver.current_url

