import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME
import allure

# Создаем константы c адресом ендпоинта
Base_URL = "https://reqres.in/"
List_Users = "api/users?page=2"
Single_User = "api/users/2"
Not_Found_User = "api/users/23"
EMAIL_ENDS = "reqres.in"
AVATAR_ENDS = "-image.jpg"


##Тест для list_User
@allure.suite('Проверка get запросов')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'делаем запрос по адресу: {Base_URL + List_Users}'):
        response = httpx.get(Base_URL + List_Users)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    with allure.step('Проверяем данные пользователей'):
        data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEME)

    with allure.step('Проверяем данные email адреса'):
        assert item['email'].endswith(EMAIL_ENDS)
        
    with allure.step('Проверяем наличие id в ссылке на аватарку'):
        assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)


##Тест для single_user
@allure.suite('Проверка get запросов')
@allure.title('Проверяем одного пользователя')
def test_single_users():
    with allure.step(f'делаем запрос по адресу: {Base_URL + Single_User}'):
        response = httpx.get(Base_URL + Single_User)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    with allure.step('Проверяем данные пользователя'):
        data = response.json()['data']

    with allure.step('Проверяем данные email адреса'):
        assert data['email'].endswith(EMAIL_ENDS)

    with allure.step('Проверяем наличие id в ссылке на аватарку'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)


##Тест для user_not_found
@allure.suite('Проверка get запросов')
@allure.title('Проверяем что пользователь не найден')
def test_user_not_found():
    with allure.step(f'делаем запрос по адресу: {Base_URL + Not_Found_User}'):
        response = httpx.get(Base_URL + Not_Found_User)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404
