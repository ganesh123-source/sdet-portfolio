from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from datetime import datetime

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def screenshot(self,name):
        os.makedirs("reports",exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S") 
        filename = f"reports/{name}_{ts}.png"
        self.driver.save_screenshot(filename)
        return filename

    