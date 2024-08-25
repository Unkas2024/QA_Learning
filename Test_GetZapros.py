import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME

 #Создаем константы c адресом ендпоинта
Base_URL = "https://reqres.in/"
List_res = "api/unknown"
Single_res = "api/unknown/2"
Single_not = "api/unknown/23"
Email_Ends = "@reqres.in"

##Тест для list_resource
def test_list_res ():
    response = httpx.get(Base_URL + List_res)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEME)


#Тест для single_resource
def test_single_res ():
    response = httpx.get(Base_URL + Single_res)
    assert response.status_code == 200
    print(response)
    data = response.json()['data']
    validate (data, USER_DATA_SCHEME)


##Тест для single_not
def test_single_not ():
   response = httpx.get(Base_URL + Single_not)
   assert response.status_code == 404
        #print(response)

