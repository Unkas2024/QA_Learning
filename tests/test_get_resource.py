import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEME
import allure

from tests.Test_user_data import List_Users

# Создаем константы c адресом ендпоинта
Base_URL = "https://reqres.in/"
List_resource = "api/unknown"
Single_resource = "api/unknown/2"
Resource_not_found = "api/unknown/23"


##Тест для list_resource
@allure.suite('Проверка get запросов')
@allure.title('Проверяем список ресурсов')
def test_list_resource():
    with allure.step(f'делаем запрос по адресу: {Base_URL + List_resource}'):
        response = httpx.get(Base_URL + List_resource)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    with allure.step('Проверяем данные о ресурсах'):
        data = response.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEME)


# Тест для single_resource
@allure.suite('Проверка get запросов')
@allure.title('Проверяем один ресурс')
def test_single_resource():
    with allure.step(f'делаем запрос по адресу: {Base_URL + Single_resource}'):
        response = httpx.get(Base_URL + Single_resource)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    with allure.step('Проверяем данные о ресурсе'):
        data = response.json()['data']

    data = response.json()['data']
    validate(data, RESOURCE_DATA_SCHEME)


##Тест для resource_not_found
@allure.suite('Проверка get запросов')
@allure.title('Проверяем что ресурс не найден')
def test_resource_not_found():
    with allure.step(f'делаем запрос по адресу: {Base_URL + Resource_not_found}'):
        response = httpx.get(Base_URL + Resource_not_found)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404
