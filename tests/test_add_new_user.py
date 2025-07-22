import allure
import pytest
from api_client import ApiClient
from data import TestData
from helper import generate_user_data

api = ApiClient()


@allure.feature("User Registration")
class TestAddNewUser:
    @allure.story("Создание уникального пользователя")
    @allure.title("Проверка успешного создания нового пользователя с валидными данными")
    def test_add_unique_user(self, created_user):
        response = created_user['response']

        with allure.step("Проверяем успешный ответ"):
            assert response.status_code == TestData.success_register_response['status_code']
            response_data = response.json()
            assert response_data['success'] == TestData.success_register_response['success']
            assert 'accessToken' in response_data
            assert 'refreshToken' in response_data

    @allure.story("Создание дубликата пользователя")
    @allure.title("Проверка создания пользователя, который уже зарегистрирован")
    def test_add_double_user(self, created_user):
        user_data = created_user['user_data']

        with allure.step("Повторная регистрация с теми же данными"):
            response = api.post("/auth/register", json=user_data)

        with allure.step("Проверяем ошибку дублирования"):
            assert response.status_code == TestData.double_register_response['status_code']
            assert response.json()['message'] == TestData.double_register_response['message']

    @allure.story("Создание пользователя без заполнения обязательного поля")
    @allure.title("Проверка создания пользователя с незаполненным полем")
    @pytest.mark.parametrize("field_to_remove, expected_message", [
        ("email", "Email, password and name are required fields"),
        ("password", "Email, password and name are required fields"),
        ("name", "Email, password and name are required fields")
    ])
    def test_add_invalid_data_user(self, user_data, field_to_remove, expected_message):
        invalid_data = user_data.copy()
        invalid_data.pop(field_to_remove)

        with allure.step(f"Регистрация без поля {field_to_remove}"):
            response = api.post("/auth/register", json=invalid_data)

        with allure.step("Проверяем ошибку валидации"):
            assert response.status_code == TestData.missing_data_register_response['status_code']
            assert response.json()['message'] == expected_message