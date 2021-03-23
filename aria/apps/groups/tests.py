from aria.apps.groups.logics import create_group
import pytest
from aria.tests.fixtures import temp_group

@pytest.mark.django_db
def test_create_group(temp_group: temp_group):
    assert create_group(temp_group.name) is False
