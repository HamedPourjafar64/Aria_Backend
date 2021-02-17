import pytest
from aria.tests.fixtures import temp_user
from aria.apps.user.logics import create_user

@pytest.mark.django_db
def test_create_user(temp_user: temp_user):
    assert create_user(temp_user) == True


@pytest.mark.django_db
def test_assign_to_group(temp_user: temp_user):
    assert assign_user_to_group(temp_user) == True


@pytest.mark.django_db
def test_update_token_password(temp_user: temp_user):
    token = 10000
    assert update_token_password(temp_user, token) == True


def test_send_token(temp_user: temp_user):
    assert send_token(temp_user) == True