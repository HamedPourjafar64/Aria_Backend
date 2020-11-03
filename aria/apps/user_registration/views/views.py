from django.conf import settings

import requests

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from aria.apps.user_registration.utils import *
from aria.apps.user_registration.communication.email.email_utils import Email, EmailUtils
from aria.apps.user_registration.communication.sms.sms_utils import SMS, SMSUtils
from aria.apps.user_registration.serializers.serializers import UserSerializer
from aria.apps.user_registration.settings import UserRegistrationSettings


@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    print(f'register json response {data}')
    # if UserRegistrationSettings.USER_NAME_FIELD == 'phone_number':
    #     if validate_phone_number(data):
    #         register_by_sms(user_name=data)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     if validate_email(data):
    #         register_by_email(user_name=data)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def validate(request):
    data = JSONParser().parse(request)
    print(f'what is the response of validate: {data}')
    # validation_status = token_validation(data, data)
    # if validation_status:
    #     # do login user and return token response
    #     login_user(user_name=data['user_name'], password=data['token'])
    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)


def register_by_sms(user_name):
    token = generate_token(user_name=user_name)
    sms = SMS(token=token, phone_number=user_name)
    SMSUtils.send_kaveh_negar_sms(sms=sms)


def register_by_email(user_name):
    token = generate_token(user_name=user_name)
    email = Email(receiver=user_name, message=token, subject='')
    EmailUtils.send_email(email=email)


# this method saves randomly generated token for a specific user
def generate_token(user_name):
    user = settings.AUTH_USER_MODEL.objects.get(pk=user_name)
    if user is None:
        create_user(user_name=user_name)
    token = generate_random_number()
    save_users_token(user_name=user_name, token=token)
    return token


def token_validation(token, user_name):
    user = settings.AUTH_USER_MODEL.objects.get(pk=user_name)
    if user.password == token:
        return True
    else:
        return False


def create_user(user_name):
    serializer = UserSerializer(data={
        UserRegistrationSettings.USER_NAME_FIELD: user_name
    })
    if serializer.is_valid():
        serializer.save()


def save_users_token(user_name, token):
    user = settings.AUTH_USER_MODEL.objects.get(pk=user_name)
    data = {'password': token}
    serializer = UserSerializer(user, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()


def login_user(user_name, password):
    data = {
        'client_id': UserRegistrationSettings.CLIENT_ID,
        'grant_type': UserRegistrationSettings.GRANT_TYPE,
        'user_name': user_name,
        'password': password
    }
    response = requests.post(UserRegistrationSettings.AUTHORIZATION_PATH, data)
    if response.status_code == 200:
        return response
    else:
        raise NameError('Could not login due to wrong credentials!')
