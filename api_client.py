import requests
import allure
from curl import BASE_URL

class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {"Content-Type": "application/json"}

    @allure.step("POST {endpoint}")
    def post(self, endpoint, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = {**self.headers, **(headers or {})}
        return requests.post(url, json=json, headers=final_headers)

    @allure.step("DELETE {endpoint}")
    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = {**self.headers, **(headers or {})}
        return requests.delete(url, headers=final_headers)

    @allure.step("GET {endpoint}")
    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = {**self.headers, **(headers or {})}
        return requests.get(url, headers=final_headers)