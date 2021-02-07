from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    creation_date = models.DateTimeField(default=datetime.now, null=False)
    user = models.ForeignKey(to=User, null=False, on_delete=models.CASCADE)
    parts = models.ManyToManyField(to='part.Part')
    services = models.ManyToManyField(to='service.Service')
