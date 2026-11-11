import pytest
import allure
import requests
from urls import URL
from generators import generate_courier_data


@allure.step("Отправляем запрос на регистрацию курьера")
def register_courier(payload):
    return requests.post(f"{URL.MAIN_URL}{URL.CREATE_COURIER}", data=payload)


@allure.step("Отправляем запрос на авторизацию курьера")
def authorize_courier(payload):
    return requests.post(f"{URL.MAIN_URL}{URL.LOGIN_COURIER}", data=payload)


@allure.step("Отправляем запрос на удаление курьера")
def delete_courier(courier_id):
    return requests.delete(f"{URL.MAIN_URL}{URL.DELETE_COURIER}{courier_id}")


@pytest.fixture
def registered_courier():
    courier = generate_courier_data()

    response = register_courier(courier)

    assert response.status_code == 201
    
    yield courier

    auth_data = {
                'login': courier['login'],
                'password': courier['password']
    }

    auth_response = authorize_courier(auth_data)
    courier_id = auth_response.json()['id']
    delete_courier(courier_id)


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

        auth_response = authorize_courier(auth_data)
        courier_id = auth_response.json()['id']
        delete_courier(courier_id)