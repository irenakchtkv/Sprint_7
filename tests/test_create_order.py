import pytest
import requests
import allure
import data
from urls import URL

class TestCreateOrder:


    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], [], None])
    @allure.title("Создание заказа с цветом: {color}")
    @allure.description("Тест проверяет успешное оформление заказа с различными вариантами выбора цвета, "
                        "включая пустой список и полное отсутствие параметра color. "
                        "Ожидаемый результат - статус 201 и наличие track  в ответе.")
    def test_create_order_successful(self, color):
        test_data = data.order_data.copy()

        test_data['color'] = color

        if color is None:
            del test_data['color']

        response = requests.post(f"{URL.MAIN_URL}{URL.ORDER_ENDPOINT}", json = test_data)

        assert response.status_code == 201
        assert "track" in response.json()
        assert type(response.json()["track"]) == int