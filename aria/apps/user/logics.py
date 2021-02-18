from aria.apps.groups.logics import create_group, group_exist
from aria.apps.user.serializers import UserSerializer
from django.contrib.auth.models import User, Group





def assign_user_to_group(group: Group, user: User):
    if group_exist(group) == False:
        create_group(group)
    user.groups.add(group.id)
    return True


def update_token_password(user: User, token):
    serializer = UserSerializer(instance=user, data={'password': token}, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False

