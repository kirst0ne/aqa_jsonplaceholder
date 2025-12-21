from helpers.validators import validate_user
import pytest

def test_get_users(client):
    response = client.get_users()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    expected_keys = {"id", "name", "username", "email", "address", "phone", "website", "company"}
    for item in data:
        assert isinstance(item, dict)
        assert expected_keys.issubset(item.keys())

@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_exists_users(client, user_id):
    response = client.get_user(user_id)
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
    validate_user(user)

@pytest.mark.parametrize("invalid_id", [11, 100])
def test_get_nonexistent_user_by_id(client, invalid_id):
    response = client.get_user(invalid_id)
    assert response.status_code == 404

def test_create_user(client, new_user_data):
    response = client.create_user(new_user_data)
    assert response.status_code == 201
    created_user = response.json()
    assert "id" in created_user
    assert created_user["id"] == 11

def test_update_user(client, random_user_id, update_user_data):
    response_update_user = client.update_user(random_user_id, update_user_data)
    assert response_update_user.status_code == 200
    updated_user = response_update_user.json()
    assert updated_user["name"] == update_user_data["name"]
    assert updated_user["email"] == update_user_data["email"]

def test_negative_test_update_user(client, max_user_id, update_user_data):
    negative_random_user_id = max_user_id + 1
    response_update_user = client.update_user(negative_random_user_id, update_user_data)
    assert response_update_user.status_code == 500

def test_delete_user(client, random_user_id):
    response = client.delete_user(random_user_id)
    assert response.status_code == 200
