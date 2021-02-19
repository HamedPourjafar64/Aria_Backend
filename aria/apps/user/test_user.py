import pytest
from aria.tests.fixtures import temp_user, temp_group
from aria.apps.user.logics import assign_user_to_group, authenticate_user, login_user, update_token_password, check_user_assigned_to_group, user_exist


@pytest.mark.django_db
def test_create_user():
    assert authenticate_user(username='+14378862841') == True


@pytest.mark.django_db
def test_user_exist(temp_user: temp_user):
    assert user_exist(temp_user.username) == True

@pytest.mark.django_db
def test_update_token_password(temp_user: temp_user):
    assert update_token_password(temp_user) == True

@pytest.mark.django_db
def test_user_assigned(temp_user):
    assign_user_to_group(temp_user)
    assert check_user_assigned_to_group(temp_user) == True
    
@pytest.mark.django_db
def test_login_user(temp_user):
    response = login_user(username=temp_user.username, password=temp_user.password)
    assert response.ok == True
