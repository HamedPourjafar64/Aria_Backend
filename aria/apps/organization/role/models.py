from django.db import models
from django.conf import settings


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=64, null=False)
    organizations = models.ManyToManyField(to='organization.Organization')
    users = models.ManyToManyField(to=settings.AUTH_USER_MODEL)
