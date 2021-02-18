import pytest
from aria.tests.fixtures import temp_user, temp_group
from aria.apps.user.logics import assign_user_to_group, update_token_password


@pytest.mark.django_db
def test_assign_user_to_group(temp_group: temp_group, temp_user: temp_user):
    assign_user_to_group(temp_group, temp_user)
    assert temp_user.groups.filter(name=temp_group.name).exists() == True
    

@pytest.mark.django_db
def test_update_token_password(temp_user: temp_user):
    token = 10000
    assert update_token_password(temp_user, token) == True
