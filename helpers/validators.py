def validate_post(post_data):
    required_fields = {"userId", "id", "title", "body"}

    missing = required_fields - set(post_data.keys())
    assert not missing, f"Отсутсвуют поля: {missing}"

    assert isinstance(post_data["userId"], int)
    assert isinstance(post_data["id"], int)
    assert isinstance(post_data["title"], str)
    assert isinstance(post_data["body"], str)

    return True

def validate_user(user_data):
    required_fields = {"id", "name", "username", "email", "address", "phone", "website", "company"}

    missing = required_fields - set(user_data.keys())
    assert not missing, f"Отсутсвуют поля: {missing}"

    assert isinstance(user_data["id"], int)
    assert isinstance(user_data["name"], str)
    assert isinstance(user_data["username"], str)
    assert isinstance(user_data["email"], str) and "@" in user_data["email"]
    assert isinstance(user_data["phone"], str)
    assert isinstance(user_data["website"], str)
    if "address" in user_data:
        assert isinstance(user_data["address"], dict)
    if "company" in user_data:
        assert isinstance(user_data["company"], dict)

    return True