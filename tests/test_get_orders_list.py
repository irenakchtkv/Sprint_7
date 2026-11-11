import requests
import allure
from urls import URL


class TestGetOrderList:


    @allure.step("Отправляем запрос на получение списка заказов")
    def get_order_list(self):
        return requests.get(f"{URL.MAIN_URL}{URL.ORDER_ENDPOINT}")


    @allure.title("Получение списка заказов")
    @allure.description("Тест проверяет успешное получение списка заказов без передачи параметров запроса. "
                        "Ожидаемый результат: статус 200, значение по ключу 'orders' является списком.")
    def test_get_order_list_successful(self):

        response = self.get_order_list()

        assert response.status_code == 200
        assert type(response.json()["orders"]) == list