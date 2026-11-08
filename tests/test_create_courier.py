import pytest
import requests
import allure
from urls import URL
from generators import generate_courier_data

class TestCreateCourier:
    

    def test_create_courier_success(self, courier_cleanup):
        payload = courier_cleanup['payload']

        response = requests.post(f"{URL.MAIN_URL}{URL.CREATE_COURIER}", data = payload)

        if response.status_code == 201 and response.json()['ok']:
            courier_cleanup['created'] = True

        assert response.status_code == 201
        assert response.json() == {"ok": True}


    def test_create_two_same_couriers_fail(self, courier_cleanup):
        payload = courier_cleanup['payload']

        first_response = requests.post(f"{URL.MAIN_URL}{URL.CREATE_COURIER}", data = payload)

        if first_response.status_code == 201 and first_response.json()['ok']:
            courier_cleanup['created'] = True
        
        assert first_response.status_code == 201
        assert first_response.json() == {"ok": True}

        second_response = requests.post(f"{URL.MAIN_URL}{URL.CREATE_COURIER}", data = payload)

        assert second_response.status_code == 409
        assert second_response.json()['message'] == 'Этот логин уже используется'


    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_without_required_field(self, missing_field):
        payload = generate_courier_data()

        del payload[missing_field]

        response = requests.post(f"{URL.MAIN_URL}{URL.CREATE_COURIER}", data = payload)

        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'