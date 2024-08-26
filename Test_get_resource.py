import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEME


# Создаем константы c адресом ендпоинта
Base_URL = "https://reqres.in/"
List_resource = "api/unknown"
Single_resource = "api/unknown/2"
Resource_not_found = "api/unknown/23"


##Тест для list_resource
def test_list_resource ():
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
