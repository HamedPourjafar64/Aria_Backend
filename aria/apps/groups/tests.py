import pytest


def test_create_group(temp_group):
    assert create_group(temp_group) == True
    
def test_assign_user_to_group(temp_group, temp_user):
    assert assign_user_to_group(temp_group, temp_user) == True