from django.db import models


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=64, null=False)
    organizations = models.ManyToManyField(to='organization.Organization')
