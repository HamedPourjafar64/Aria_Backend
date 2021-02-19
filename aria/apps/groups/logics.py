from os import name
from aria.apps.groups.serializers import GroupSerializer
from django.contrib.auth.models import Group


def create_group(groupname):
    data = {
        'name': groupname
    }
    serializer = GroupSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False

def group_exist(groupname):
    if Group.objects.filter(name=groupname).count() > 0:
        return True
    return False