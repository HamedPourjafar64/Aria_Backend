from django.db import models
from datetime import datetime
from .car_types import CarTypes
from .car import Car


class CarImages(models.Model):
    name = models.CharField(max_length=64, null=True)
    file = models.ImageField(upload_to='media/images/cars/%Y/%m/%d/', null=True, blank=True)
    upload_date = models.DateTimeField(default=datetime.now, null=True)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    type = models.IntegerField(choices=CarTypes.choices(), default=CarTypes.SEDAN)
