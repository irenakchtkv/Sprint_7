import pytest
import generators 
import requests
from urls import URL
from generators import generate_courier_data

@pytest.fixture
def registered_courier():
    courier = generators.register_new_courier_and_return_login_password()

    yield courier

    auth_response = requests.post(f"{URL.MAIN_URL}{URL.LOGIN_COURIER}", data = courier)

    courier_id = auth_response.json()['id']
    requests.delete(f"{URL.MAIN_URL}{URL.DELETE_COURIER}{courier_id}")
# есть один потенциальный риск: если регистрация курьера не удалась,
# фикстура всё равно попытается авторизоваться и получить id
# Это может привести к дополнительной ошибке при очистке.


@pytest.fixture
def courier_cleanup():
    courier = {
        'payload': generate_courier_data(),
        'created': False
    }
    
    yield courier

    if courier['created'] == True:

        auth_data = {
                    'login': courier['payload']['login'],
                    'password': courier['payload']['password']
        }

        auth_response = requests.post(f"{URL.MAIN_URL}{URL.LOGIN_COURIER}", data = auth_data)
        courier_id = auth_response.json()['id']
        requests.delete(f"{URL.MAIN_URL}{URL.DELETE_COURIER}{courier_id}")
    