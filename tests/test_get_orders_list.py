import requests
import allure
from urls import URL

class TestGetOrderList:

    @allure.title("Получение списка заказов")
    @allure.description("Тест проверяет успешное получение списка заказов без передачи параметров запроса. "
                        "Ожидаемый результат: статус 200, значение по ключу 'orders' является списком.")
    def test_get_order_list_successful(self):

        response = requests.get(f"{URL.MAIN_URL}{URL.ORDER_ENDPOINT}")

        assert response.status_code == 200
        assert type(response.json()["orders"]) == list