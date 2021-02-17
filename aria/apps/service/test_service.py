from aria.apps.service.logics import create_service
import pytest
from aria.tests.fixtures import temp_service, temp_service_category, temp_part


@pytest.mark.django_db
def test_create_service(temp_service):
    assert create_service(temp_service) == True