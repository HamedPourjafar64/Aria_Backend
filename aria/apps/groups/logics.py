from os import name
from aria.apps.groups.serializers import GroupSerializer
from django.contrib.auth.models import Group


def create_group(group):
    serializer = GroupSerializer(data=group)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False

def group_exist(group: Group):
    if Group.objects.filter(name=group.name).count() > 0:
        return True
    return False