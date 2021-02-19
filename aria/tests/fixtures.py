from aria.apps.aria_profile.logics import create_profile
from aria.apps.service.logics import create_service
from aria.apps.aria_address.logics import create_address
from aria.apps.vehicle.logics.add import create_vehicle
from aria.apps.part.logics import create_part
from aria.apps.service.service_category.logics import create_service_category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.contrib.auth.models import Group
import pytest
import os


@pytest.fixture(autouse=True)
def temp_user(django_user_model):
    return django_user_model.objects.create(
        username='tester', password='tester@123')

@pytest.fixture
def temp_group():
    return Group.objects.create(name='test')


@pytest.fixture
def temp_part():
    return {
        "name": "Test",
        "price": 200,
        "quantity": 100,
        "unit": "Litr"
    }


@pytest.fixture
def temp_service_category():
    return {
        "name": "Test",
        "image": SimpleUploadedFile(name='test.jpg',
                                    content=open(os.path.join(settings.BASE_DIR, 'test.jpg'), 'rb').read(), content_type='image/jpeg'),
        "enabled": True
    }


@pytest.fixture
def temp_service(temp_service_category, temp_part):
    create_service_category(temp_service_category)
    create_part(temp_part)
    return {
        "name": "Test",
        "description": "Testing",
        "price": 200,
        "in_place": False,
        "is_transfer": True,
        "service_worker_fee": 200,
        "category": 1,
        "parts": 1
    }


@pytest.fixture
def temp_address():
    return {
        'country': 'Canada',
        'city': 'Vancouver',
        'street': 'bst',
        'latitude': 25.3,
        'longitude': 25.3,
        'user': 1
    }


@pytest.fixture
def temp_vehicle():
    return {
        'user': 1,
        'model': "racing",
        'year': 1995,
        'manufacturer': "kawazaki",
        'vehicle_type': "Motor-Cycle",
    }


@pytest.fixture
def temp_order(temp_address, temp_service, temp_vehicle):
    create_vehicle(vehicle=temp_vehicle)

    create_address(address=temp_address)

    create_service(service=temp_service)

    return {
        'src_addr': 1,
        'order_time': '1995-08-26T19:56:38',
        "user": 1,
        'services': 1
    }


@pytest.fixture
def temp_profile():
    return {
        'f_name': 'hamed',
        'l_name': 'pourjafar',
        'full_name': 'hamed pourjafar',
    }


@pytest.fixture
def temp_contact(temp_address, temp_profile):
    create_address(address=temp_address)
    create_profile(profile=temp_profile, username='tester')
    return {
        "fax_number": "0933333",
        "name": "work",
        "email": "hppourjafar@g",
        "address": 1,
        "profile" : 1
    }
