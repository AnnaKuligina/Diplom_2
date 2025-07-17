import allure
import pytest
from api_client import ApiClient
from data import TestData
from helper import generate_user_data

api = ApiClient()


@allure.feature("User Registration")
class TestAddNewUser:
    @pytest.fixture
    def user_data(self):

        return generate_user_data()

    @allure.story("Создание уникального пользователя")
    @allure.title("Проверка успешного создания нового пользователя с валидными данными")
    def test_add_unique_user(self, user_data): # Проверка создания уникального пользователя
        with allure.step("Отправляем запрос на регистрацию"):
            response = api.post("/auth/register", json=user_data)

        with allure.step("Проверяем успешный ответ"):
            assert response.status_code == TestData.success_register_response['status_code']
            response_data = response.json()
            assert response_data['success'] == TestData.success_register_response['success']
            assert 'accessToken' in response_data
            assert 'refreshToken' in response_data

        with allure.step("Удаляем тестового пользователя"):
            token = response_data['accessToken']
            api.delete("/auth/user", headers={"Authorization": f"Bearer {token}"})

    @allure.story("Создание дубликата пользователя")
    @allure.title("Проверка создания пользователя, который уже зарегистрирован")
    def test_add_double_user(self, user_data): # Проверка создания пользователя, который уже зарегистрирован
        with allure.step("Первая регистрация пользователя"):
            first_response = api.post("/auth/register", json=user_data)
            assert first_response.status_code == 200
            token = first_response.json()['accessToken']

        with allure.step("Повторная регистрация с теми же данными"):
            second_response = api.post("/auth/register", json=user_data)

        with allure.step("Проверяем ошибку дублирования"):
            assert second_response.status_code == TestData.double_register_response['status_code']
            assert second_response.json()['message'] == TestData.double_register_response['message']

        with allure.step("Удаляем тестового пользователя"):
            api.delete("/auth/user", headers={"Authorization": f"Bearer {token}"})

    @allure.story("Создание пользователя без заполнения обязательного поля")
    @allure.title("Проверка создания пользователя с незаполненным полем")
    @pytest.mark.parametrize("field_to_remove, expected_message", [
        ("email", "Email, password and name are required fields"),
        ("password", "Email, password and name are required fields"),
        ("name", "Email, password and name are required fields")
    ])
    def test_add_invalid_data_user(self, user_data, field_to_remove, expected_message): # Проверка создания пользователя с одним незаполненным полем
        invalid_data = user_data.copy()
        invalid_data.pop(field_to_remove)

        with allure.step(f"Регистрация без поля {field_to_remove}"):
            response = api.post("/auth/register", json=invalid_data)

        with allure.step("Проверяем ошибку валидации"):
            assert response.status_code == TestData.missing_data_register_response['status_code']
            assert response.json()['message'] == expected_message