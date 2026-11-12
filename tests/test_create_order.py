import pytest
import allure
import data
from API_client import APIClient

class TestCreateOrder:

    client = APIClient()

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

        response = self.client.create_order(test_data)

        assert response.status_code == 201
        assert "track" in response.json()
        assert type(response.json()["track"]) == int