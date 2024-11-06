import httpx


# Создаем константы c адресом ендпоинта
Base_URL = "https://reqres.in/"
Unlogin_user = "api/login"


def test_unlogin_user():
    body = {
        "email": "peter@klaven"
    }

    response = httpx.post(Base_URL + Unlogin_user, json=body)
    print(response.json())
    assert response.status_code == 400
    print(response.status_code)
