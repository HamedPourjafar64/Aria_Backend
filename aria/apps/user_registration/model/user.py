from django.db import models
from django.contrib.auth.models import AbstractUser
from aria.apps.user_registration.settings import UserRegistrationSettings as Settings
from aria.apps.user_registration.model.custom_manager import CustomManager


class User(AbstractUser):
    phone_number = models.CharField(max_length=32, null=False, default='', unique=True,
                                    primary_key=True if Settings.USER_NAME_FIELD == 'phone_number' else False, )
    email = models.EmailField(max_length=64, null=False, default='', unique=True,
                              primary_key=True if Settings.USER_NAME_FIELD == 'email' else False, )
    password = models.CharField(max_length=128, null=False, default='Aria#123')

    username = phone_number if Settings.USER_NAME_FIELD == 'phone_number' else email

    USERNAME_FIELD = 'phone_number' if Settings.USER_NAME_FIELD == 'phone_number' else 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def __str__(self):
        return self.username
