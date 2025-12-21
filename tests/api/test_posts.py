from helpers.validators import validate_post
from tests.api.conftest import client


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

def test_get_exists_posts(client, posts_data):
    valid_ids = posts_data.get("valid_ids", [1, 50, 100])
    for post_id in valid_ids:
        response = client.get_post(post_id)
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id
        validate_post(post)

def test_get_nonexists_random_post_id(client, posts_data):
    invalid_id = posts_data.get("invalid_id", 999)
    response = client.get_post(invalid_id)
    assert response.status_code == 404

def test_create_post(client, new_post_data):
    response = client.create_post(new_post_data)
    assert response.status_code == 201
    created_post = response.json()
    assert "id" in created_post
    assert created_post["id"] == 101

def test_update_post(client, random_post_id, update_post_data):
    response_update_post = client.update_post(random_post_id, update_post_data)
    assert response_update_post.status_code == 200
    updated_post = response_update_post.json()
    assert updated_post["title"] == update_post_data["title"]
    assert updated_post["body"] == update_post_data["body"]
    assert updated_post["userId"] == update_post_data["userId"]
    assert updated_post["id"] == random_post_id

def test_negative_test_update_post(client, max_post_id, update_post_data):
    negative_random_post_id = max_post_id + 1
    response_update_post = client.update_post(negative_random_post_id, update_post_data)
    assert response_update_post.status_code == 500

def test_delete_post(client, random_post_id):
    response = client.delete_post(random_post_id)
    assert response.status_code == 200
