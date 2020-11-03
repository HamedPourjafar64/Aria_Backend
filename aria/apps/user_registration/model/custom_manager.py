from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomManager(BaseUserManager):
    """
    we need to verify in manager level that phone number is the user unique username
    """

    def create_user(self, phone_number, password, **extra_fields):
        """
        create and save User with given phone_number and password
        """
        if not phone_number:
            raise ValueError(_('The Phone_Number  is required'))
        user = self.model(phone_no=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        """
        Create and save a Super User with the given phone number and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Super User must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Super User must have is_superuser=True'))
        return self.create_user(phone_no=phone_number, password=password, **extra_fields)
