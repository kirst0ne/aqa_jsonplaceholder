import requests
from helpers.config import Config
from helpers.logger import get_logger

class ApiClient:
    def __init__(self):
        self.base_url = Config.API.base_url
        self.timeout = Config.API.timeout
        self.session = requests.Session()
        self.logger = get_logger(__name__)

    def _make_request(self, method, endpoint, **kwargs):
        """Базовый метод для всех запросов"""
        url = f"{self.base_url}/{endpoint}"
        self.logger.info(f"{method.upper()} {url}")
        # Выбираем метод
        request_method = getattr(self.session, method.lower())
        # Делаем запрос
        response = request_method(url, timeout = self.timeout, **kwargs)
        self.logger.info(f"Response: {response.status_code}")
        return response


    def get_posts(self):
        return self._make_request("GET", "posts")

    def get_post(self, post_id):
        return self._make_request("GET", f"posts/{post_id}")

    def create_post(self, post_data):
        return self._make_request("POST", "posts", json=post_data)

    def get_users(self):
        return self._make_request("GET", "users")

    def get_user(self, user_id):
        return self._make_request("GET", f"users/{user_id}")

    def create_user(self, user_data):
        return self._make_request("POST", "users", json=user_data)

    def update_post(self, post_id, update_data):
        return self._make_request("PUT", f"posts/{post_id}", json=update_data)

    def update_user(self, user_id, update_data):
        return self._make_request("PUT", f"users/{user_id}", json=update_data)

    def delete_post(self, post_id):
        return self._make_request("DELETE", f"posts/{post_id}")

    def delete_user(self, user_id):
        return self._make_request("DELETE", f"users/{user_id}")