import pytest
from helpers.api_client import ApiClient

@pytest.fixture()
def client():
    return ApiClient("https://jsonplaceholder.typicode.com")

@pytest.fixture()
def new_post_data():
    return {
        "title": "Test-Title for POST",
        "body": "Test-Body for POST",
        "userId": 6
      }

@pytest.fixture()
def new_user_data():
    return {
        "name": "Test User",
        "username": "Test Username",
        "email": "testuser@example.com"
    }