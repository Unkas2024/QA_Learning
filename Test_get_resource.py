import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEME, USER_DATA_SCHEME


# Создаем константы c адресом ендпоинта
Base_URL = "https://reqres.in/"
List_Users = "api/users?page=2"
Single_User = "api/users/2"
Not_Found_User = "api/users/23"
List_resource = "api/unknown"
Single_resource = "api/unknown/2"
Resource_not_found = "api/unknown/23"
EMAIL_ENDS = "reqres.in"
AVATAR_ENDS = "-image.jpg"


##Тест для list_User
def test_list_users():
    response = httpx.get(Base_URL + List_Users)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEME)
    assert item['email'].endswith(EMAIL_ENDS)
    assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

    ##Тест для single_user


def test_single_users():
    response = httpx.get(Base_URL + Single_User)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['email'].endswith(EMAIL_ENDS)
    assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

##Тест для user_not_found
def test_user_not_found():
    response = httpx.get(Base_URL + Not_Found_User)
    assert response.status_code == 404


##Тест для list_resource
def test_list_resource():
    response = httpx.get(Base_URL + List_resource)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEME)


# Тест для single_resource
def test_single_resource():
    response = httpx.get(Base_URL + Single_resource)
    assert response.status_code == 200
    print(response)
    data = response.json()['data']
    validate(data, RESOURCE_DATA_SCHEME)


##Тест для resource_not_found
def test_resource_not_found():
    response = httpx.get(Base_URL + Resource_not_found)
    assert response.status_code == 404
