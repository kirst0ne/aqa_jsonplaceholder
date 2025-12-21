import pytest
import random
import requests
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
def update_post_data(posts_data):
    """Данные для создания нового поста"""
    return posts_data.get("update_post", {})

@pytest.fixture(scope="session")
def all_post_ids():
    """Все ID постов - кешируем через scope="session" """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return [post["id"] for post in response.json()]

@pytest.fixture()
def random_post_id(all_post_ids):
    return random.choice(all_post_ids)

@pytest.fixture()
def max_post_id(all_post_ids):
    return max(all_post_ids)

@pytest.fixture()
def users_data(test_data):
    """Данные для тестов пользователей"""
    return test_data.get("users", {})

@pytest.fixture()
def new_user_data(users_data):
    """Данные для создания нового пользователя"""
    return users_data.get("new_user", {})

@pytest.fixture()
def update_user_data(users_data):
    """Данные для создания нового поста"""
    return users_data.get("update_user", {})

@pytest.fixture(scope = "session")
def all_user_ids():
    """Все ID пользователей - кешируем через scope="session" """
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return [user["id"] for user in response.json()]

@pytest.fixture()
def random_user_id(all_user_ids):
    return random.choice(all_user_ids)

@pytest.fixture()
def max_user_id(all_user_ids):
    return max(all_user_ids)
