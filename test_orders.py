    # Даниил Дунаев, 15-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import sender_stand_request

def test_get_order_by_tracking_number():

    # Запрос на получение заказа
    response_get = requests.get(configuration.URL_SERVICE + configuration.CREATE_GIVE_PATH, params={'t': sender_stand_request.response.json().get('track')})
    assert response_get.status_code == 200, "Ошибка при получении заказа. Статус код: {response_get.status_code}"

    # Проверяем содержание ответа
    order_details = response_get.json()
    assert 'order' in order_details, "Ответ не содержит информацию о заказе"
    print("Готово, детали заказа:", order_details)

def test_get_order_without_tracking_number():
    # Запрос на получение заказа без номера
    response_get = requests.get(configuration.URL_SERVICE + configuration.CREATE_GIVE_PATH)
    assert response_get.status_code == 400, "Ожидался статус код 400 при запросе без номера трека"

def test_get_order_with_invalid_tracking_number():
    # Запрос на получение заказа с несуществующим номером
    response_get = requests.get(configuration.URL_SERVICE + configuration.CREATE_GIVE_PATH, params={'t': 'invalid_number'})
    assert response_get.status_code == 404, "Ожидался статус код 404 при запросе с несуществующим номером"
