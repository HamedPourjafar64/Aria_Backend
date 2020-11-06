from django.db import models
from django.conf import settings


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=128, null=False)
    email = models.CharField(max_length=128, null=True)
    phone_number = models.CharField(max_length=32, null=True)
    profile_pic = models.ImageField(upload_to='/media/profile/%Y/%m/%d/', null=True, blank=True)
    bio = models.CharField(max_length=256, null=True)
