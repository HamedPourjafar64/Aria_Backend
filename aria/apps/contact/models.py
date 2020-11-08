from django.db import models


# Create your models here.
class Contact(models.Model):
    home_phone_number = models.CharField(max_length=32, null=True)
    mobile_phone_number = models.CharField(max_length=32, null=True)
    address = models.OneToOneField(to='address.Address', on_delete=models.CASCADE, null=True)
    fax_number = models.CharField(max_length=32, null=True)
    assigned_name = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=128, null=False)
