from django.db import models
from .car_types import CarTypes
from django.conf import settings


class Car(models.Model):
    manufacturer = models.CharField(max_length=64, null=False)
    type = models.IntegerField(
        choices=[(carType, carType.value) for carType in CarTypes],
        default=1,
        null=False
    )
    model = models.CharField(max_length=128, null=False)
    year = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
