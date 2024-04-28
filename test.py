import configuration
import sender_stand_request
import requests

# Проверка статуса ответа
if sender_stand_request.response.status_code == 201:
    tracking_number = sender_stand_request.response.json().get('track')
    print(f"Заказ успешно создан, вот его номер: {tracking_number}")
    # Запрос на получение заказа
    response_get = requests.get(
        f"{configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH}/track",
        params={'t': tracking_number}
    )

    if response_get.status_code == 200:
        order_details = response_get.json()
        print("Готово, детали заказа:", order_details)
    else:
        print(
            "Ошибка при получении заказа. "
            f"Статус код: {response_get.status_code}"
        )
else:
    print(
        f"Ошибка при создании заказа. Статус код: {sender_stand_request.response.status_code}"
    )