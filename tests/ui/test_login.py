import pytest

@pytest.mark.smoke
@pytest.mark.ui
def test_login_page_loads(login_page):
    """Login page opens and has correct title"""
    login_page.open()
    assert "The Internet" in login_page.driver.title

@pytest.mark.smoke
@pytest.mark.ui
def test_valid_login_redirects(login_page):
    """Valid credentials redirect to /secure"""
    login_page.login("tomsmith","SuperSecretPassword!")
    assert "secure" in login_page.driver.current_url

@pytest.mark.regression
@pytest.mark.ui
def test_valid_login_message(login_page):
    """Valid login shows success flash message"""
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area" in login_page.get_message()

@pytest.mark.regression
@pytest.mark.ui
def test_invalid_login_message(login_page):
    """Invalid credentials show error message"""
    login_page.login("wornguser","wrongpass")
    assert "Your username is invalid" in login_page.get_message()

@pytest.mark.regression
@pytest.mark.ui
def test_logout(logged_in,secure_page):
    """After login, logout redirects back to login page"""
    secure_page.click_logout()
    assert "login" in secure_page.get_url()

@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize("username,password,expected",[
        ("tomsmith",  "SuperSecretPassword!", "secure area"),
        ("wronguser", "wrongpass", "username is invalid"),
        ("tomsmith",  "wrongpass", "password is invalid"),  
    ],ids=["valid", "wrong-user", "wrong-pass"])
def test_login_scenerios(username,password,expected,login_page):
    """Multiple login scenarios with different credentials"""
    login_page.login(username,password)
    assert expected.lower() in login_page.get_message().lower() 




