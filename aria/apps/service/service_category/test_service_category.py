from aria.apps.service.service_category.logics import create_service_category
import pytest
from aria.tests.fixtures import temp_service_category


@pytest.mark.django_db
def test_create_service_category(temp_service_category):
    assert create_service_category(service_category=temp_service_category) == True
