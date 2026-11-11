import pytest
import requests
import allure
import data
from urls import URL

class TestCreateOrder:


    @allure.step("Отправляем запрос на создание заказа")
    def create_order(self, payload):
        return requests.post(f"{URL.MAIN_URL}{URL.ORDER_ENDPOINT}", json=payload)


    @pytest.mark.parametrize('test_data', [
        data.create_order_data(['BLACK']), 
        data.create_order_data(['GREY']), 
        data.create_order_data(['BLACK', 'GREY']), 
        data.create_order_data([]), 
        data.create_order_data(None)
        ])
    @allure.title("Создание заказа с определенным цветом")
    @allure.description("Тест проверяет успешное оформление заказа с различными вариантами выбора цвета, "
                        "включая пустой список и полное отсутствие параметра color. "
                        "Ожидаемый результат - статус 201 и наличие track в ответе.")
    def test_create_order_successful(self, test_data):

        response = self.create_order(test_data)

        assert response.status_code == 201
        assert "track" in response.json()
        assert type(response.json()["track"]) == int