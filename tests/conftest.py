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
    register_response = api.post("/auth/register", json=user_data)
    assert register_response.status_code == 200

    login_response = api.post("/auth/login", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })
    token = login_response.json()["accessToken"]

    if not token.startswith("Bearer "):
        token = f"Bearer {token}"

    yield {
        "user_data": user_data,
        "token": token,
        "headers": {"Authorization": token}
    }

    # Удаление пользователя
    api.delete("/auth/user", headers={"Authorization": token})