from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import IntEnum
from aria.apps.user_registration.settings import UserRegistrationSettings as Settings
from aria.apps.user_registration.model.custom_manager import CustomManager


class Role(IntEnum):
    COMPANY_ADMIN = 1
    SYSTEM_ADMIN = 2
    SERVICE_WORKER = 3
    COMPANY_EMPLOYEE = 4
    NORMAL_USER = 5

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class User(AbstractUser):
    phone_number = models.CharField(max_length=32, null=False, default='', unique=True,
                                    primary_key=True if Settings.USER_NAME_FIELD == 'phone_number' else False, )
    email = models.EmailField(max_length=64, null=False, default='', unique=True,
                              primary_key=True if Settings.USER_NAME_FIELD == 'email' else False, )
    password = models.CharField(max_length=128, null=False, default='Aria#123')
    role = models.IntegerField(choices=Role.choices(), default=Role.NORMAL_USER)

    username = None

    USERNAME_FIELD = 'phone_number' if Settings.USER_NAME_FIELD == 'phone_number' else 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def get_user_role_title(self):
        return Role(self.role).name.title()

    def __str__(self):
        return self.phone_number
