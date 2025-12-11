import requests

def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0