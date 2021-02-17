from aria.apps.aria_profile.models import AriaProfile
from aria.apps.aria_profile.logics import create_profile, update_profile
import pytest
from aria.tests.fixtures import temp_user, temp_profile




@pytest.fixture
def old_temp_profile():
    return AriaProfile(pk=1)


@pytest.mark.django_db
def test_create_profile(temp_profile: temp_profile):
    assert create_profile(temp_profile, 'tester') == True

@pytest.mark.django_db
def test_update_profile(old_temp_profile, temp_profile: temp_profile):
    assert update_profile(old_temp_profile, temp_profile, 'tester') == True
