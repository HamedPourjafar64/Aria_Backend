from django.db import models
from enum import IntEnum


class CarTypes(IntEnum):
    # car types enum
    SEDAN = 1
    COUPE = 2
    SPORTS_CAR = 3
    STATION_WAGON = 4
    HATCHBACK = 5
    CONVERTIBLE = 6
    SUV = 7
    MINIVAN = 8
    PICKUP_TRUCK = 9

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


# Create your models here.
class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=64, null=False)
    is_car = models.BooleanField(default=True)
    car_type = models.IntegerField(
        choices=CarTypes.choices(),
        default=1,
        null=True
    )
    vehicle_type = models.CharField(max_length=250, null=False)
    model = models.CharField(max_length=128, null=False)
    year = models.IntegerField()
    # profile = models.ForeignKey(to='profile.Profile', on_delete=models.CASCADE)


class VehicleImages(models.Model):
    file = models.ImageField(upload_to='media/images/cars/%Y/%m/%d/', null=True, blank=True)
    vehicle = models.ForeignKey(to=Vehicle, on_delete=models.CASCADE)
