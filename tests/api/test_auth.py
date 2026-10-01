import requests
import pytest

@pytest.mark.smoke
@pytest.mark.api
def test_valid_login(api_base):
    """Valid API login returns 200 and a token"""
    response = requests.post(f"{api_base}/auth/login", json= {"username": "emilys","password": "emilyspass"})
    assert response.status_code == 200, "login failed"
    assert "accessToken" in response.json()
    assert isinstance(response.json()["accessToken"], str)

@pytest.mark.smoke
@pytest.mark.api
def test_invalid_login(api_base):
    """Wrong password returns 400"""
    response = requests.post(
        f"{api_base}/auth/login",
        json={"username": "emilys", "password": "wrongpass"}
    )
    assert response.status_code == 400

@pytest.mark.regression
@pytest.mark.api
def test_get_current_user(api_base,auth_token):
    """Token can be used to get current user data"""
    response = requests.get(f"{api_base}/auth/me",headers={"Authorization":f"Bearer {auth_token}"})
    assert response.status_code ==200
    user = response.json()
    assert "firstName" in user
    assert "email" in user

@pytest.mark.regression
@pytest.mark.api
def test_expired_token_returns_401(api_base):
    """Wrong token returns 401"""
    response = requests.get(f"{api_base}/auth/me",headers= {"Authorization":"Bearer fakeToken18737"})
    assert response.status_code == 401
