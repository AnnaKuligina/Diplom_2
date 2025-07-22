import pytest
import allure
from api_client import ApiClient
from helper import generate_user_data

api = ApiClient()


@pytest.fixture
def user_data():
    with allure.step("Генерация данных пользователя"):
        return generate_user_data()


@pytest.fixture
def created_user(user_data):
    # Регистрация пользователя
    response = api.post("/auth/register", json=user_data)
    assert response.status_code == 200
    token = response.json()['accessToken']

    yield {
        'user_data': user_data,
        'token': token,
        'response': response
    }
    # Удаление пользователя после теста
    with allure.step("Удаление тестового пользователя"):
        api.delete("/auth/user", headers={"Authorization": f"Bearer {token}"})
