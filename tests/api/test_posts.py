import pytest

from helpers.validators import validate_post

def test_get_all_posts(client):
    response = client.get_posts()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    expected_keys = {"userId", "id", "title", "body"}
    for item in data:
        assert isinstance(item, dict)
        assert expected_keys.issubset(item.keys())

@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_exists_posts(client, post_id):
    response = client.get_post(post_id)
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    validate_post(post)

def test_get_nonexists_random_post_id(client):
    response = client.get_post(999)
    assert response.status_code == 404

def test_create_post(client, new_post_data):
    response = client.create_post(new_post_data)
    assert response.status_code == 201

    created_post = response.json()
    assert "id" in created_post
    assert created_post["id"] == 101
