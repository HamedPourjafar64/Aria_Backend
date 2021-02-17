from aria.apps.part.logics import create_part
import pytest
from aria.tests.fixtures import temp_part

@pytest.mark.django_db
def test_create_part(temp_part):
    assert create_part(part=temp_part) == True

