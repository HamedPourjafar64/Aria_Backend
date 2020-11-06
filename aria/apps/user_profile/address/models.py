from django.db import models


# Create your models here.
class Address(models.Model):
    country = models.CharField(max_length=32, null=False)
    city = models.CharField(max_length=64, null=False)
    district = models.CharField(max_length=32, null=True)
    street = models.CharField(max_length=128, null=False)
    apartment_number = models.CharField(max_length=32, null=True)
    pin_point_location = models.CharField(max_length=128, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=3)
    longitude = models.DecimalField(max_digits=30, decimal_places=3)
    profile = models.ForeignKey(to='user_profile.Profile', on_delete=models.CASCADE)
