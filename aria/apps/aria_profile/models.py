from django.db import models
from django.conf import settings


class AriaProfile(models.Model):
    full_name = models.CharField(max_length=128, null=True)
    f_name = models.CharField(max_length=64, null=True)
    l_name = models.CharField(max_length=64, null=False)
    image = models.ImageField(
        upload_to='media/images/profile/%Y/%m/%d/', null=True, blank=True)
    bio = models.CharField(max_length=256, null=True)
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    contact = models.ForeignKey(
        to='aria_contact.Contact', on_delete=models.CASCADE, null=True)