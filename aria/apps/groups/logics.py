from aria.apps.groups.serializers import GroupSerializer


def create_group(group):
    serializer = GroupSerializer(data=group)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False

def group_exist(group):
    print('test')