from aria.apps.aria_address.logics import create_address
import pytest
from aria.tests.fixtures import temp_address, temp_user

@pytest.mark.django_db
def test_create_address(temp_address):
    assert create_address(address=temp_address) == True