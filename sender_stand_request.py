import requests
import data
import configuration

def post_new_orders(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
        json=body,
        headers=data.headers,
    )
response = post_new_orders(data.orders_body)

def create_order():

    # Запрос на создание заказа
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH, json=data.orders_body)
    assert response.status_code == 201, f"Ошибка при создании заказа. Статус код: {response.status_code}"

    # Сохраняем номер заказа
    tracking_number = response.json().get('track')
    assert tracking_number is not None, "Номер не возвращен"

    return tracking_number