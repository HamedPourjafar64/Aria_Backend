import pytest
from aria.apps.vehicle.logics.add import create_vehicle, validate_vehicle_data


@pytest.fixture
def temp_vehicle(django_user_model):
    django_user_model.objects.create(
        username='testerzings', password='tester@123')

    return {
        'user': '1',
        'model': "racing",
        'year': 1995,
        'manufacturer': "kawazaki",
        'vehicle_type': "Motor-Cycle",
    }


# def test_vehicle_data(vehicle):
#     assert validate_vehicle_data(vehicle) == True

@pytest.mark.django_db
def test_create_vehicle(temp_vehicle):
    assert create_vehicle(temp_vehicle) == True
