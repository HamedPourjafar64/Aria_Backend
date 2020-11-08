from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=64, null=False)
    contact = models.OneToOneField(to='contact.Contact', on_delete=models.CASCADE)
