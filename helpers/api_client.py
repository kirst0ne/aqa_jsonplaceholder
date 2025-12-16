import requests
from helpers.config import Config

class ApiClient:
    def __init__(self):
        self.base_url = Config.API.base_url
        self.timeout = Config.API.timeout
        self.session = requests.Session()

    def get_posts(self):
        return self.session.get(f"{self.base_url}/posts")

    def get_post(self, post_id):
        return self.session.get(f"{self.base_url}/posts/{post_id}")

    def create_post(self, post_data):
        return self.session.post(f"{self.base_url}/posts", json=post_data)

    def get_users(self):
        return self.session.get(f"{self.base_url}/users")

    def get_user(self, user_id):
        return self.session.get(f"{self.base_url}/users/{user_id}")

    def create_user(self, user_data):
        return self.session.post(f"{self.base_url}/users", json=user_data)
