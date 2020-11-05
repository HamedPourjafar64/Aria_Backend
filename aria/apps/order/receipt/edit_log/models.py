from django.db import models
from django.conf import settings
from datetime import datetime


# Create your models here.
class EditLog(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
    date = models.DateTimeField(default=datetime.now, null=False)
    reason = models.CharField(max_length=256, null=False)
    receipt = models.ForeignKey(to='aria.apps.order.receipt.Receipt', on_delete=models.CASCADE)
