import allure
import pytest
from data import TestData
from api_client import ApiClient

api = ApiClient()


@allure.feature("Order Creation")
class TestCreateOrder:
    @allure.story("Заказ с авторизацией")
    @allure.title("Создание заказа с авторизацией пользователя")
    def test_create_order_with_login(self, created_user): # Проверка создания заказа с авторизацией пользователя
        headers = {"Authorization": created_user["token"]}

        response = api.post(
            "/orders",
            json=TestData.valid_order,
            headers=headers
        )

        assert response.status_code == 200, f"Ошибка: {response.text}"
        response_data = response.json()
        assert response_data["success"] is True
        assert "order" in response_data
        assert "number" in response_data["order"]

    @allure.story("Заказ без авторизации")
    @allure.title("Создание заказа без авторизации пользователя")
    def test_create_order_without_login(self): # Проверка создания заказа без авторизации пользователя
        response = api.post("/orders", json=TestData.valid_order)
        assert response.status_code in [200, 401], f"Неожиданный статус: {response.status_code}"

    @allure.story("Проверка ингредиентов")
    @allure.title("Проверка корректности ингредиентов в заказе")
    def test_create_order_with_ingredients(self, created_user): # Проверка создания заказа с ингредиентами
        headers = {"Authorization": created_user["token"]}

        response = api.post(
            "/orders",
            json=TestData.valid_order,
            headers=headers
        )

        assert response.status_code == 200
        ingredients = response.json()["order"]["ingredients"]
        assert len(ingredients) == len(TestData.valid_ingredients)
        assert all(ing["_id"] in TestData.valid_ingredients for ing in ingredients)

    @allure.story("Заказ без ингредиентов")
    @allure.title("Попытка создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self, created_user): # Проверка создания заказа без ингредиентов
        headers = {"Authorization": created_user["token"]}

        response = api.post(
            "/orders",
            json=TestData.empty_order,
            headers=headers
        )

        assert response.status_code == 400
        assert not response.json()["success"]
        assert "ingredient" in response.json().get("message", "").lower()

    @allure.story("Неверные ингредиенты")
    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_wrong_ingredients(self, created_user): # Проверка создания заказа с неверным хешем ингредиентов
        headers = {"Authorization": created_user["token"]}

        response = api.post(
            "/orders",
            json=TestData.invalid_order,
            headers=headers
        )

        assert response.status_code in [400, 500], f"Неожиданный статус: {response.status_code}"

        try:
            response_data = response.json()
            if response.status_code == 500:
                assert False, "Сервер вернул 500 ошибку с JSON-ответом: " + str(response_data)
            assert not response_data["success"]
        except ValueError:
            if response.status_code == 500:
                assert True
            else:
                assert False, f"Не удалось получить ответ: {response.text}"