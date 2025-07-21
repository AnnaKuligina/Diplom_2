import allure
import pytest
from api_client import ApiClient

api = ApiClient()


@allure.feature("Авторизация пользователя")
class TestLoginUser:
    @allure.title("Тест успешного входа с валидными данными")
    def test_login_existing_user(self, created_user): # Проверка успешности входа существующего пользователя с валидными данными
        with allure.step("Отправка запроса на вход с валидными данными"):
            response = api.post("/auth/login", json={
                "email": created_user["user_data"]["email"],
                "password": created_user["user_data"]["password"]
            })

        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 200, \
                f"Ожидался код 200, получен {response.status_code}. Ответ: {response.text}"
            response_json = response.json()
            assert "accessToken" in response_json, \
                f"AccessToken не найден в ответе. Ответ: {response_json}"

    @allure.title("Тест неуспешного входа с невалидными данными")
    @pytest.mark.parametrize("invalid_data", [
        {"email": "wrong@example.com", "password": "password"},
        {"password": "password"},
        {"email": "test@example.com"}
    ])
    def test_login_invalid_data_user(self, invalid_data): # Проверка логина пользователя с неверными данными
        with allure.step(f"Отправка запроса с невалидными данными: {invalid_data}"):
            response = api.post("/auth/login", json=invalid_data)

        with allure.step("Проверка неуспешного ответа"):
            assert response.status_code == 401, \
                f"Ожидался код 401, получен {response.status_code}. Ответ: {response.text}"
