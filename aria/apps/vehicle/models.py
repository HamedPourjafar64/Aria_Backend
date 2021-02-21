from django.db import models
from django.conf import settings

# Create your models here.

class VehicleImages(models.Model):
    file = models.ImageField(upload_to='media/images/vehicles/%Y/%m/%d/', null=True, blank=True)

class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=64, null=False)
    vehicle_type = models.CharField(max_length=250, null=False)
    model = models.CharField(max_length=128, null=False)
    year = models.IntegerField()
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle_images = models.ForeignKey(to=VehicleImages, on_delete=models.CASCADE)


