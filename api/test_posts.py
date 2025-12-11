import requests

def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0