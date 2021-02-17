from aria.apps.order.logics.create_order import create, validate_order
from aria.tests.fixtures import *
import pytest

def test_order_validation(temp_order: temp_order):
    assert validate_order(temp_order) == True


@pytest.mark.django_db
def test_create_order(temp_order: temp_order):
    create(temp_order)

