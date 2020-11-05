from django.db import models
from django.conf import settings


# Create your models here.
class ServiceWorker(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
