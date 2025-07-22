Во второй части дипломной работы мною реализованы тесты API для сервиса Stellar Burgers.

Содержание: 
1) allure_results - сгенерированный Allure-отчёт 
2) tests - тестовые сценарии
3) curl.ру - URL-адреса используемых страниц
4) data.ру - тестовые данные
5) helper.ру - методы для генерирования данных
6) requirements.txt - файл с внешними зависимостями
7) api_client - перечень используемых при тестировании api

В папке tests находится: -conftest.ру где хранятся фикстуры,
а так же, в папке tests находятся тестовые сценарии

1) "Создание пользователя" 
- test_add_unique_user 
- test_add_double_user 
- test_add_invalid_data_user 
2) "Логин пользователя" 
- test_login_existing_user 
- test_login_invalid_data_user 
3) "Создание заказа" 
- test_create_order_with_login 
- test_create_order_without_login 
- test_create_order_with_ingredients 
- test_create_order_without_ingredients 
- test_create_order_wrong_ingredients