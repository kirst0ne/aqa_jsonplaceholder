from pkg_resources import invalid_marker

from helpers.validators import validate_user

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

def test_get_exists_users(client, users_data):
    valid_ids = users_data.get("valid_ids", [1, 5, 10])
    for user_id in valid_ids:
        response = client.get_user(user_id)
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == user_id
        print(f"response: {user}")
        validate_user(user)

def test_get_nonexists_user(client, users_data):
    invalid_id = users_data.get("invalid_id", 11)
    response = client.get_user(invalid_id)
    assert response.status_code == 404

def test_create_user(client, new_user_data):
    response = client.create_user(new_user_data)
    assert response.status_code == 201
    created_user = response.json()
    assert "id" in created_user
    assert created_user["id"] == 11
