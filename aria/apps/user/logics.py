import requests


from aria.apps.user.utils import generate_random_number
from django.conf import settings
from aria.apps.user.communication.sms import send_sms
from aria.apps.user.phone_validator.phone_validator import validate_phone_number
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
    raise ValueError('Username is not valid!')


def create_user(username):
    data = {
        'username': username,
        'password': username + '@' + username[0:2]
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()


def check_username(username):
    if validate_phone_number(username):
        return True
    return False


def user_exist(username):
    if User.objects.filter(username=username).count() > 0:
        return True
    return False


def update_token_password(user: User):
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


def login_user(username, password):
    if check_username(username=username) and user_exist(username):
        user_data = {
            'username': 'hamed',
            'password': 'Hamed@123'
        }
        data = {
            'client_id': 'jckmJoDYbAcpWHzB9jpaYj3gRfeew8YYjeViEviL',
            'client_secret': 'XI9ZoyhwsEp6iCHXA7wTbyyS1H4buFdZhS0GhSDcfafx6y8dSPxGoXdAClfvAbdYpGHf67CYXoAkODvdSgqjYsEBpl2bdiLYgESDciRTKgJOGyBouPXctOj9loVT5kUR',
            'grant_type': 'password'
        }
        data.update(user_data)
        response = requests.post(
            url='http://localhost:8000/authentication/token/', data=data,)
        return response
    return {}
