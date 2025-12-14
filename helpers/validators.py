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
    if "phone" in user_data:
        assert isinstance(user_data["phone"], str)
    if "website" in user_data:
        assert isinstance(user_data["website"], str)
    if "address" in user_data:
        assert isinstance(user_data["address"], dict)

        required_fields_address = {"street", "suite", "city", "zipcode", "geo"}
        address_data = user_data["address"]

        missing_address = required_fields_address - set(address_data.keys())
        assert not missing_address, f"Отсутствуют поля: {missing_address}"

        if "geo" in address_data:
            assert isinstance(address_data["geo"], dict)
            required_fields_geo = {"lat", "lng"}
            geo_data = address_data["geo"]

            missing_geo = required_fields_geo - set(geo_data.keys())
            assert not missing_geo, f"Отсутствуют поля: {missing_geo}"

    if "company" in user_data:
        assert isinstance(user_data["company"], dict)

        required_fields_company = {"name", "catchPhrase", "bs"}
        company_data = user_data["company"]

        missing_company = required_fields_company - set(company_data.keys())
        assert not missing_company, f"Отсутствуют поля: {missing_company}"

    return True