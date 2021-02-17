import pytest
from aria.apps.vehicle.logics.add import create_vehicle
from aria.tests.fixtures import temp_vehicle, temp_user


@pytest.mark.django_db
def test_create_vehicle(temp_vehicle: temp_vehicle):
    assert create_vehicle(temp_vehicle) == True
