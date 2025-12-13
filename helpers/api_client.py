import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get_posts(self):
        return self.session.get(f"{self.base_url}/posts")

    def get_post(self, post_id):
        return self.session.get(f"{self.base_url}/posts/{post_id}")

    def get_users(self):
        return self.session.get(f"{self.base_url}/users")

    def get_user(self, user_id):
        return self.session.get(f"{self.base_url}/users/{user_id}")
