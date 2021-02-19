from django.conf import settings
from aria.apps.user.communication.sms import send_sms
from aria.apps.user.phone_validator.phone_validator import validate_phone_number
from aria.apps.groups.logics import create_group, group_exist
from aria.apps.user.serializers import UserSerializer
from django.contrib.auth.models import User, Group
import random


def generate_random_number():
    return random.randint(10000, 99999)


def create_user(username):
    if check_username(username):
        if user_exist(username) is False:
            data = {
                'username': username,
                'password': username + '@' + username[0:2]
            }
            serializer = UserSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        user = User.objects.get(username=username)
        update_token_password(user=user)
        group = Group(name=settings.REGISTER_GROUP)
        if user_assigned(user=user, group=group):
            assign_user_to_group(group=group, user=user)
        return True
    raise ValueError('Username is not valid!')


def assign_user_to_group(group: Group, user: User):
    if group_exist(group) == False:
        create_group(group)
    user.groups.add(group.id)
    return True


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


def check_username(username):
    # we need to check for phone number validation
    if validate_phone_number(username):
        return True
    return False


def user_exist(username):
    if check_username(username):
        if User.objects.filter(username=username).count() > 0:
            return True
        return False
    return False


def user_assigned(user: User, group: Group):
    groups = user.groups.all()
    for gr in groups:
        if gr.name == group.name:
            return True
    return False
