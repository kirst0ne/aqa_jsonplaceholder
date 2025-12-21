from helpers.validators import validate_user
import pytest
import allure

@allure.feature("Users API")
@allure.story("GET operations")
class TestUsers:
    @allure.title("Get all users")
    def test_get_users(self, client):
        with allure.step("Send /GET users request"):
            response = client.get_users()

        with allure.step("Check response status code"):
            assert response.status_code == 200

        with allure.step("Check response structure"):
            data = response.json()
            assert isinstance(data, list)
            assert len(data) > 0
            expected_keys = {"id", "name", "username", "email", "address", "phone", "website", "company"}
            for item in data:
                assert isinstance(item, dict)
                assert expected_keys.issubset(item.keys())

    @allure.title("Positive - Get user by ID: {user_id}")
    @pytest.mark.parametrize("user_id", [1, 5, 10])
    def test_get_exists_users(self, client, user_id):
        with allure.step(f"Send /GET /users{user_id} request"):
            response = client.get_user(user_id)

        with allure.step("Check response status code"):
            assert response.status_code == 200

        with allure.step("Check response structure"):
            user = response.json()
            assert user["id"] == user_id
            validate_user(user)

    @allure.title("Negative - Get user by invalid ID: {invalid_id}")
    @pytest.mark.parametrize("invalid_id", [11, 100])
    def test_get_nonexistent_user_by_id(self, client, invalid_id):
        with allure.step(f"Send /GET /users{invalid_id} request"):
            response = client.get_user(invalid_id)

        with allure.step("Check response status code"):
            assert response.status_code == 404
    @allure.title("Create new user")
    def test_create_user(self, client, new_user_data):
        with allure.step("Send /POST /users request"):
            response = client.create_user(new_user_data)
        with allure.step("Check response status code"):
            assert response.status_code == 201
        with allure.step("Check response structure"):
            created_user = response.json()
            assert "id" in created_user
            assert created_user["id"] == 11

    @allure.title("Positive - Update user")
    def test_update_user(self, client, random_user_id, update_user_data):
        with allure.step(f"Send /UPDATE /users/{random_user_id} request"):
            response_update_user = client.update_user(random_user_id, update_user_data)

        with allure.step("Check response status code"):
            assert response_update_user.status_code == 200

        with allure.step("Check response structure"):
            updated_user = response_update_user.json()
            assert updated_user["name"] == update_user_data["name"]
            assert updated_user["email"] == update_user_data["email"]

    @allure.title("Negative - Update user")
    def test_negative_test_update_user(self, client, max_user_id, update_user_data):
        negative_random_user_id = max_user_id + 1
        with allure.step(f"Send /UPDATE /users/{negative_random_user_id}"):
            response_update_user = client.update_user(negative_random_user_id, update_user_data)

        with allure.step("Check response status code"):
            assert response_update_user.status_code == 500

    @allure.title("Delete user")
    def test_delete_user(self, client, random_user_id):
        with allure.step(f"Send /DELETE /users/{random_user_id}"):
            response = client.delete_user(random_user_id)

        with allure.step("Check response status code"):
            assert response.status_code == 200
