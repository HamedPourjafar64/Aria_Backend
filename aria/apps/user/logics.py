from aria.apps.user.serializers import UserSerializer


def create_user(user):
    serializer = UserSerializer(data=user)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False


def assign_user_to_group(user):
    print('test')