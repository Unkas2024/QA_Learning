from venv import create

import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEME
import datetime

# Создаем константы c адресом ендпоинта
Base_URL = "https://reqres.in/"
Create_User = "api/users"
Update_user = "api/users/2"


# def test_create_user():
#    body = {
#        "name": "morpheus",
#        "job": "leader"
#    }

#    response = httpx.post(Base_URL + Create_User, json = body)
#    print (response.json())
#       assert response.status_code == 201

def test_update_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = httpx.put(Base_URL + Update_user, json=body)
    assert response.status_code == 200

    validate(response.json(), CREATED_USER_SCHEME)

    creation_date = response.json()['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    assert creation_date[0:16] == current_date[0:16]

    assert response.json()['name'] == body['name']
    assert response.json()['job'] == body['job']


def test_update_all_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = httpx.patch(Base_URL + Update_user, json=body)
    assert response.status_code == 200

    validate(response.json(), CREATED_USER_SCHEME)

    creation_date = response.json()['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    assert creation_date[0:16] == current_date[0:16]
    assert response.json()['name'] == body['name']
    assert response.json()['job'] == body['job']


def test_delete_user():
    response = httpx.delete(Base_URL + Update_user)
