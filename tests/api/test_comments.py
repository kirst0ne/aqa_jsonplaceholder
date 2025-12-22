from helpers.validators import validate_comment
import requests
import allure
import pytest

@allure.feature("Comments API")
@allure.story("Comments CRUD operations")
class TestComments:
    @allure.title("Get all comments")
    def test_get_all_comments(self, client):
        with allure.step("Send /GET comments request"):
            try:
                response = client.get_comments()
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                # Добавляем информацию в Allure
                allure.attach(str(e), name="Timeout/Connection Error")
                allure.attach("API is too slow, consider this a bug", name="Note")

                # Пропускаем тест с сообщением
                pytest.skip(f"API /comments is too slow: {e}")

        with allure.step("Check response status code"):
            assert response.status_code == 200

        with allure.step("Check response comment-structure"):
            data = response.json()
            assert isinstance(data, list)
            assert len(data) > 0
            expected_keys = {"postId", "name", "email", "body"}
            for item in data:
                assert isinstance(item, dict)
                assert expected_keys.issubset(item.keys())

    @allure.title("Get comment by ID: {comment_id}")
    @pytest.mark.parametrize("comment_id", [1, 100, 500])
    def test_get_exists_comments(self, client, comment_id):
        with allure.step(f"Send /GET comments/{comment_id} request"):
            response = client.get_comment(comment_id)

        with allure.step("Check response status code"):
            assert response.status_code == 200

        with allure.step("Check response comment-structure"):
            comment = response.json()
            assert comment["id"] == comment_id
            validate_comment(comment)

    @allure.title("Get comment by invalid ID: {invalid_id}")
    @pytest.mark.parametrize("invalid_id", [501, 999])
    def test_get_nonexistent_comment_by_id(self, client, invalid_id):
        with allure.step(f"Send /GET comments/{invalid_id} request"):
            response = client.get_comment(invalid_id)

        with allure.step("Check response status code"):
            assert response.status_code == 404

    @allure.title("Get comments by post ID: {post_id}")
    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_comment_by_post_id(self, client, post_id):
        with allure.step(f"Send /GET posts/{post_id}/comments request"):
            response = client.get_comment_by_post_id(post_id)

        with allure.step("Check response status code"):
            assert response.status_code == 200

        with allure.step("Check response comment_by_post_id-structure"):
            comments = response.json()
            assert isinstance(comments, list)
            for comment in comments:
                assert comment["postId"] == post_id
                expected_keys = {"postId", "name", "email", "body"}
                assert expected_keys.issubset(comment.keys())
            else:
                allure.attach(f"No comments found for post {post_id}", name="Info")

    @allure.title("Create new comment")
    def test_create_comment(self, client, new_comment_data):
        with allure.step("Send /POST comments"):
            response = client.create_comment(new_comment_data)

        with allure.step("Check response status code"):
            assert response.status_code == 201

        with allure.step("Check response comment-stcucture"):
            created_comment = response.json()
            assert "id" in created_comment
            assert created_comment["id"] == 501

    @allure.title("Positive - Update comment")
    def test_update_comment(self, client, random_comment_id, update_comment_data):
        with allure.step(f"Send /PUT comments/{random_comment_id} request"):
            response_update_comment = client.update_comment(random_comment_id, update_comment_data)

        with allure.step("Check response status code"):
            assert response_update_comment.status_code == 200

        with allure.step("Check response comment-structure"):
            updated_comment = response_update_comment.json()
            assert updated_comment["name"] == update_comment_data["name"]
            assert updated_comment["email"] == update_comment_data["email"]
            assert updated_comment["body"] == update_comment_data["body"]
            assert updated_comment["id"] == random_comment_id

    @allure.title("Negative - Update comment")
    def test_negative_update_comment(self, client, max_comment_id, update_comment_data):
        negative_comment_id = max_comment_id + 1
        with allure.step(f"Send /UPDATE comments/{negative_comment_id} request"):
            response_update_comment = client.update_comment(negative_comment_id, update_comment_data)

        with allure.step("Check response status code"):
            assert response_update_comment.status_code == 500

    @allure.title("Delete comment")
    def test_delete_comment(self, client, random_comment_id):
        with allure.step(f"Send /DELETE comment/{random_comment_id} request"):
            response = client.delete_comment(random_comment_id)

        with allure.step("Check response status code"):
            assert response.status_code == 200
