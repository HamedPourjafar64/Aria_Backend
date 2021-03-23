import requests


from aria.apps.user.utils import generate_random_number
from django.conf import settings
from aria.apps.user.communication.sms import send_sms
from aria.apps.user.phone_validator.phone_validator import is_valid_phone
from aria.apps.groups.logics import create_group, group_exist
from aria.apps.user.serializers import UserSerializer
from django.contrib.auth.models import User, Group


def authenticate_user(username):
    if check_username(username):
        if user_exist(username) is False:
            create_user(username=username)
        user = User.objects.get(username=username)
        update_token_password(user=user)
        check_user_assigned_to_group(user=user)
        return True
    return False


def create_user(username):
    data = {
        'username': username,
        'password': username + '@' + username[0:2]
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()


def check_username(username):
    if is_valid_phone(username):
        return True
    return False


def user_exist(username):
    if User.objects.filter(username=username).count() > 0:
        return True
    return False


def update_token_password(user: User):
    # token = generate_random_number()
    token = 10000
    serializer = UserSerializer(
        instance=user, data={'password': token}, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # send_sms(token, user.username)
        return True
    return False


def check_user_assigned_to_group(user: User):
    groups = user.groups.all()
    for gr in groups:
        if gr.name == settings.REGISTER_GROUP:
            return True
    assign_user_to_group(user=user)
    return False


def assign_user_to_group(user: User):
    if group_exist(settings.REGISTER_GROUP) == False:
        create_group(settings.REGISTER_GROUP)
    group = Group.objects.get(name=settings.REGISTER_GROUP)
    user.groups.add(group)
    return True


def user_validation(username, password):
    
    data = {
        'client_id': 'v4d4C8mMqTMQ3bYoKnBJtn2oYRTgLpL4b6LInCKo',
        'client_secret': 'EoOmkh9XsmxJNTZKE5h84qIuqYsv6FOb9ZjAVq7Y4k0rugkH2FnUU2kcIwMK8827NoQGmBUBocBPzAZyxCzRTGpslCcDCNsBk66DiAsnLBZsVbl3mmxVu1hs6Q8dW4zV',
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    session = requests.Session()
    response = session.post(
        url='http://localhost:8000/authentication/token/', data=data,)
    return response
