from helpers.api_client import ApiClient

client = ApiClient("https://jsonplaceholder.typicode.com")

def test_get_users():
    response = client.get_users()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    expected_keys = {"id", "name", "username", "email", "address", "phone", "website", "company"}
    for item in data:
        assert isinstance(item, dict)
        assert expected_keys.issubset(item.keys())

test_ids = [1, 9, 10]

def test_get_exists_users():
    for user_id in test_ids:
        response = client.get_user(user_id)
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == user_id

def test_get_nonexists_user():
    response = client.get_user(11)
    assert response.status_code == 404
