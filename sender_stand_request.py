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