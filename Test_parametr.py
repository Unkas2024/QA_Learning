import json

import httpx
import pytest
from jsonschema import validate
from core.contracts import LOGIN_USER_SCHEME

Base_URL = "https://reqres.in/"
Login_User = "api/login"

json_file = open('C:/Users/pazif/PycharmProjects/API_Test/core/new_users_data.json')
user_data = json.load(json_file)


@pytest.mark.parametrize('user_data', user_data)
def test_login_success(user_data):
    response = httpx.post(Base_URL + Login_User, json=user_data)
    assert response.status_code == 200

    validate(response.json(), LOGIN_USER_SCHEME)
