from helpers.validators import validate_post
import allure
import pytest

@allure.feature("Posts API")
@allure.story("Posts CRUD operations")
class TestPosts:
    @allure.title("Get all posts")
    def test_get_all_posts(self, client):
        with allure.step("Send /GET posts request"):
            response = client.get_posts()

        with allure.step("Check response status"):
            assert response.status_code == 200

        with allure.step("Check response structure"):
            data = response.json()
            assert isinstance(data, list)
            assert len(data) > 0
            expected_keys = {"userId", "id", "title", "body"}
            for item in data:
                assert isinstance(item, dict)
                assert expected_keys.issubset(item.keys())

    @allure.title("Get post by ID: {post_id}")
    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_exists_posts(self, client, post_id):
        with allure.step(f"Send /GET posts/{post_id} request"):
            response = client.get_post(post_id)

        with allure.step("Check response"):
            assert response.status_code == 200

        with allure.step("Check response structure"):
            post = response.json()
            assert post["id"] == post_id
            validate_post(post)

    @allure.title("Get post by invalid ID: {invalid_id}")
    @pytest.mark.parametrize("invalid_id", [101, 999])
    def test_get_nonexistent_post_by_id(self, client, invalid_id):
        with allure.step(f"Send /GET posts/{invalid_id} request"):
            response = client.get_post(invalid_id)

        with allure.step("Check response status code"):
            assert response.status_code == 404

    @allure.title("Create new post")
    def test_create_post(self, client, new_post_data):
        with allure.step("Send /POST posts/ request"):
            response = client.create_post(new_post_data)

        with allure.step("Check response status code"):
            assert response.status_code == 201

        with allure.step("Check response structure"):
            created_post = response.json()
            assert "id" in created_post
            assert created_post["id"] == 101

    @allure.title("Positive - Update post")
    def test_update_post(self, client, random_post_id, update_post_data):
        with allure.step(f"Send /PUT posts/{random_post_id}"):
            response_update_post = client.update_post(random_post_id, update_post_data)

        with allure.step("Check response status code"):
            assert response_update_post.status_code == 200

        with allure.step("Check response structure"):
            updated_post = response_update_post.json()
            assert updated_post["title"] == update_post_data["title"]
            assert updated_post["body"] == update_post_data["body"]
            assert updated_post["userId"] == update_post_data["userId"]
            assert updated_post["id"] == random_post_id

    @allure.title("Negative - Update post")
    def test_negative_test_update_post(self, client, max_post_id, update_post_data):
        negative_random_post_id = max_post_id + 1

        with allure.step(f"Send /PUT posts/{negative_random_post_id}"):
            response_update_post = client.update_post(negative_random_post_id, update_post_data)

        with allure.step("Check response status code"):
            assert response_update_post.status_code == 500

    @allure.title("Delete Post")
    def test_delete_post(self, client, random_post_id):
        with allure.step(f"Send /DELETE /posts/{random_post_id}"):
            response = client.delete_post(random_post_id)

        with allure.step("Check response status code"):
            assert response.status_code == 200
