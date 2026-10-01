import pytest
import requests
from selenium import webdriver
from pages.login_page import LoginPage
from pages.securepage import SecurePage
from pages.checkboxes_page import CheckBoxes

UI_BASE = "https://the-internet.herokuapp.com"
API_BASE = "https://dummyjson.com"

@pytest.fixture
def driver():
    d = webdriver.Edge()
    d.maximize_window()
    yield d
    d.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def secure_page(driver):
    return SecurePage(driver)

@pytest.fixture
def checkboxs_page(driver):
    return CheckBoxes(driver)

@pytest.fixture
def logged_in(login_page):
    login_page.login("tomsmith","SuperSecretPassword!")
    return login_page

@pytest.fixture
def api_base():
    return "https://dummyjson.com"

@pytest.fixture
def auth_token(api_base):
    response = requests.post(f"{api_base}/auth/login", json= {"username": "emilys","password": "emilyspass"})
    assert response.status_code == 200,"API login failed — cannot get token"
    return response.json()["accessToken"]

@pytest.fixture
def api_session(auth_token):
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    })
    return session

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Auto screenshot when any UI test fails"""
    outcome = yield
    report  = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            test_name = item.name
            filename  = None
            for fixture in item.funcargs.values():
                if hasattr(fixture, "screenshot"):
                    filename = fixture.screenshot(f"FAILED_{test_name}")
                    break
            if not filename:
                from datetime import datetime
                import os
                os.makedirs("reports", exist_ok=True)
                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"reports/FAILED_{test_name}_{ts}.png"
                driver.save_screenshot(filename)
            print(f"\n📸 Screenshot: {filename}")

