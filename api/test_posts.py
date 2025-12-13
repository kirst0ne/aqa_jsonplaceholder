from helpers.api_client import ApiClient

client = ApiClient("https://jsonplaceholder.typicode.com")

def test_get_all_posts():
    response = client.get_posts()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    expected_keys = {"userId", "id", "title", "body"}
    for item in data:
        assert isinstance(item, dict)
        assert expected_keys.issubset(item.keys())

test_ids = [1, 50, 100]

def test_get_exists_posts():
    for post_id in test_ids:
        response = client.get_post(post_id)
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id


def test_get_nonexists_random_post_id():
    response = client.get_post(999)
    assert response.status_code == 404
