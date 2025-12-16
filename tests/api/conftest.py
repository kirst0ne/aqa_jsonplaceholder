import pytest
from helpers.api_client import ApiClient
from helpers.utils import load_test_data

@pytest.fixture()
def client():
    return ApiClient()

@pytest.fixture(scope="session")
def test_data():
    """Все тестовые данные"""
    return load_test_data()

@pytest.fixture()
def posts_data(test_data):
    """Данные для тестов постов"""
    return test_data.get("posts", {})

@pytest.fixture()
def new_post_data(posts_data):
    """Данные для создания нового поста"""
    return posts_data.get("new_post", {})

@pytest.fixture()
def users_data(test_data):
    """Данные для тестов пользователей"""
    return test_data.get("users", {})

@pytest.fixture()
def new_user_data(users_data):
    """Данные для создания нового пользователя"""
    return users_data.get("new_user", {})
