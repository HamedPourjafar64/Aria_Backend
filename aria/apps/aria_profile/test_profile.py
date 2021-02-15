from aria.apps.aria_profile.models import AriaProfile
from aria.apps.aria_profile.logics import create_profile, update_profile
import pytest


@pytest.fixture
def temp_profile(django_user_model):
    django_user_model.objects.create(username='tester', password='tester@123')
    return {
        'f_name': 'hamed',
        'l_name': 'pourjafar',
        'full_name': 'hamed pourjafar',
        'user': 1
    }

@pytest.fixture
def old_temp_profile():
    return AriaProfile(pk=1)


@pytest.mark.django_db
def test_create_profile(temp_profile):
    assert create_profile(temp_profile) == True

@pytest.mark.django_db
def test_update_profile(old_temp_profile, temp_profile):
    assert update_profile(old_temp_profile, temp_profile) == True
