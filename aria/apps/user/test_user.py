import pytest
from aria.tests.fixtures import temp_user, temp_group
from aria.apps.user.logics import assign_user_to_group, create_user, update_token_password, user_assigned, user_exist


@pytest.mark.django_db
def test_create_user():
    assert create_user(username='+14378862841') == True


@pytest.mark.django_db
def test_user_exist(temp_user: temp_user):
    assert user_exist(temp_user.username) == True

@pytest.mark.django_db
def test_assign_user_to_group(temp_group: temp_group, temp_user: temp_user):
    assign_user_to_group(temp_group, temp_user)
    assert temp_user.groups.filter(name=temp_group.name).exists() == True

@pytest.mark.django_db
def test_update_token_password(temp_user: temp_user):
    assert update_token_password(temp_user) == True

@pytest.mark.django_db
def test_user_assigned(temp_user, temp_group):
    assign_user_to_group(temp_group, temp_user)
    assert user_assigned(temp_user, temp_group) == True
