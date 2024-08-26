import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME


# Создаем константы c адресом ендпоинта
Base_URL = "https://reqres.in/"
List_Users = "api/users?page=2"
Single_User = "api/users/2"
Not_Found_User = "api/users/23"
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