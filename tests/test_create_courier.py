import pytest
import requests
import allure
from urls import URL
from generators import generate_courier_data


class TestCreateCourier:


    @allure.step("Отправляем запрос на регистрацию курьера")
    def create_courier(self, payload):
        return requests.post(f"{URL.MAIN_URL}{URL.CREATE_COURIER}", data=payload)

    @allure.title("Регистрация курьера")
    @allure.description("Тест проверяет успешное создание курьера с передачей всех обязательных полей. "
                        "Ожидаемый результат: статус 201, {'ok':true} в теле ответа.")
    def test_create_courier_success(self, courier_cleanup):
        payload = courier_cleanup['payload']

        response = self.create_courier(payload)

        assert response.status_code == 201

        courier_cleanup['created'] = True

        assert response.json() == {"ok": True}


    @allure.title("Регистрация двух одинаковых курьеров")
    @allure.description("Тест проверяет получение ошибки при создании двух одинаковых курьеров. "
                        "Ожидаемый результат: статус 409, тело ответа {'message': 'Этот логин уже используется'}.")
    def test_create_two_same_couriers_fail(self, registered_courier):
        payload = registered_courier

        second_response = self.create_courier(payload)

        assert second_response.status_code == 409
        assert second_response.json()['message'] == 'Этот логин уже используется'


    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    @allure.title("Регистрация курьера без поля: {missing_field}")
    @allure.description("Тест проверяет получение ошибки при отсутствии одного из обязательных полей. "
                        "Ожидаемый результат: статус 400, тело ответа {'message': 'Недостаточно данных для создания учетной записи'}.")
    def test_create_courier_without_required_field(self, missing_field):
        payload = generate_courier_data()

        del payload[missing_field]

        response = self.create_courier(payload)

        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'