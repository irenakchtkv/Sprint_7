import requests
import allure
from urls import URL

class APIClient:

    @allure.step("Отправляем запрос на регистрацию курьера")
    def register_courier(self, payload):
        return requests.post(f"{URL.MAIN_URL}{URL.CREATE_COURIER}", data=payload)


    @allure.step("Отправляем запрос на авторизацию курьера")
    def authorize_courier(self, payload):
        return requests.post(f"{URL.MAIN_URL}{URL.LOGIN_COURIER}", data=payload)


    @allure.step("Отправляем запрос на удаление курьера")
    def delete_courier(self, courier_id):
        return requests.delete(f"{URL.MAIN_URL}{URL.DELETE_COURIER}{courier_id}")


    @allure.step("Отправляем запрос на создание заказа")
    def create_order(self, payload):
        return requests.post(f"{URL.MAIN_URL}{URL.ORDER_ENDPOINT}", json=payload)


    @allure.step("Отправляем запрос на получение списка заказов")
    def get_order_list(self):
        return requests.get(f"{URL.MAIN_URL}{URL.ORDER_ENDPOINT}")