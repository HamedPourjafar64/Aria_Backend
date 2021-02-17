from aria.apps.aria_contact.logics import create_contact
import pytest
from aria.tests.fixtures import temp_contact, temp_profile, temp_user, temp_address

@pytest.mark.django_db
def test_create_contact(temp_contact):
    assert create_contact(temp_contact) == True