from django.db import models


class Contact(models.Model):
    fax_number = models.CharField(max_length=32, null=True)
    name = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=128, null=False)
    address = models.OneToOneField(to='aria_address.Address', on_delete=models.CASCADE)


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=32, null=False)
    tag_name = models.CharField(max_length=64, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
