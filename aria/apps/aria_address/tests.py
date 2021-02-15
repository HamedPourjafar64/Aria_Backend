from aria.apps.aria_address.logics import create_address, validate_address
import pytest


@pytest.fixture
def temp_address(django_user_model):
    django_user_model.objects.create(
        username='tester', password='tester@123')

    return {
        'country': 'Canada',
        'city': 'Vancouver',
        'street': 'bst',
        'latitude': 25.3,
        'longitude': 25.3,
        'user': 1
    }


def test_address_data_validation(temp_address):
    assert validate_address(temp_address) == True


@pytest.mark.django_db
def test_create_address(temp_address):
    assert create_address(temp_address) == True