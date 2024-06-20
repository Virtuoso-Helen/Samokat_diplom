# Елена Гришаева, 17-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import data
import requests


# Запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=body)


# Запрос на получение трэк номера заказа
def get_track_id(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response


# Автотест
    # Создание заказа и получение номера трека
def test_order_creation():
    response = post_new_order(data.order_body)
    track_number = response.json()["track"]

    # Получение заказа по трек-номеру
    order_response = get_track_id(track_number)
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    print("Заказ успешно создан, трэк номер:", track_number)
