from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CheckBoxes(BasePage):
    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.XPATH,"//input[@type = 'checkbox']")

    def open(self):
        self.driver.get(self.URL)

    def get_all_checkboxes(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.CHECKBOXES))

    def check_all(self):
        for box in self.get_all_checkboxes():
            if not box.is_selected():
                box.click()
    def uncheck_all(self):
        for box in self.get_all_checkboxes():
            if box.is_selected():
                box.click()
    def get_checked_count(self):
        count = 0
        for box in self.get_all_checkboxes():
            if box.is_selected():
                count +=1
        return count