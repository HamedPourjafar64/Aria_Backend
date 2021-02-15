from aria.apps.aria_address.logics import create_address
from aria.apps.vehicle.logics.add import create_vehicle
from aria.apps.order.logics.create_order import create, validate_order

import pytest


@pytest.fixture
def order(django_user_model):
    django_user_model.objects.create(
        username='tester1', password='tester@123')

    vehicle = {
        "is_car": False,
        "model": "racing",
        "year": 1995,
        "manufacturer": "kawazak",
        "vehicle_type": "Motor-Cycle",
        "user": 1
    }

    create_vehicle(info=vehicle)

    address = {
        'country': 'IR',
        'city' : 'Tehran',
        'street': 'sohrevardi',
        'latitude': 25.39,
        'longitude': 25.39,
        'user': 1
    }

    create_address(address=address)

    return {
        'src_addr': 1,
        'order_time': '1995-08-26T19:56:38',
        "user": 1,
    }



def test_order_validation(order):
    assert validate_order(order) == True


@pytest.mark.django_db
def test_create_order(order):
    create(order)
