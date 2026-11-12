import allure
from API_client import APIClient


class TestGetOrderList:

    client = APIClient()

    @allure.title("Получение списка заказов")
    @allure.description("Тест проверяет успешное получение списка заказов без передачи параметров запроса. "
                        "Ожидаемый результат: статус 200, значение по ключу 'orders' является списком.")
    def test_get_order_list_successful(self):

        response = self.client.get_order_list()

        assert response.status_code == 200
        assert type(response.json()["orders"]) == list