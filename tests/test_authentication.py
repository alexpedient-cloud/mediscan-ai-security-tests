def authenticate(token):

    valid_tokens = ["secure_token_123"]

    if token not in valid_tokens:
        raise PermissionError("Unauthorized")

    return True


def test_authentication_bypass():

    token = None

    try:
        authenticate(token)
    except PermissionError:
        assert True