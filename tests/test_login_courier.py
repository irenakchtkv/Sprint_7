import pytest
import allure
from generators import generate_random_string
from API_client import APIClient


class TestLoginCourier:

    client = APIClient()

    @allure.title("Авторизация курьера")
    @allure.description("Тест проверяет успешную авторизацию курьера с передачей всех обязательных полей. "
                        "Ожидаемый результат: статус 200, наличие id в теле ответа.")
    def test_login_courier_successful(self, registered_courier):
        payload = {
                    'login': registered_courier['login'],
                    'password': registered_courier['password']
        }

        response = self.client.authorize_courier(payload)

        assert response.status_code == 200
        assert 'id' in response.json()
        assert type(response.json()['id']) == int


    @pytest.mark.parametrize('changed_value', ['login', 'password'])
    @allure.title("Авторизация курьера c некорректным полем: {changed_value}")
    @allure.description("Тест проверяет получение ошибки при авторизации курьера с некорректным логином или паролем. "
                        "Ожидаемый результат: статус 404, тело ответа {'message': 'Учетная запись не найдена'}.")
    def test_login_courier_with_changed_credentials(self, changed_value, registered_courier):
        original_data = {
                        'login': registered_courier['login'],
                        'password': registered_courier['password']
        }

        payload = original_data.copy()

        payload[changed_value] = generate_random_string(5)

        response = self.client.authorize_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"


    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    @allure.title("Авторизация курьера без поля: {missing_field}")
    @allure.description("Тест проверяет получение ошибки при авторизации курьера без логина или пароля. "
                        "Ожидаемый результат: статус 400, тело ответа {'message': 'Недостаточно данных для входа'}.")
    def test_login_courier_without_required_field(self, missing_field, registered_courier):
        original_data = {
                        'login': registered_courier['login'],
                        'password': registered_courier['password']
        }

        payload = original_data.copy()

        del payload[missing_field]

        response = self.client.authorize_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"


    @allure.title("Авторизация курьера с несуществующей парой логин-пароль")
    @allure.description("Тест проверяет получение ошибки при авторизации курьера с несуществующей парой логин-пароль. "
                        "Ожидаемый результат: статус 404, тело ответа {'message': 'Учетная запись не найдена'}.")
    def test_login_courier_with_non_existent_credentials(self):
        payload = {
            'login': generate_random_string(7),
            'password': generate_random_string(8)
        }

        response = self.client.authorize_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"