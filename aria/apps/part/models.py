from django.db import models


class Part(models.Model):
    name = models.CharField(max_length=64, null=False)
    price = models.BigIntegerField(null=True)
    quantity = models.BigIntegerField(null=False)
    unit = models.CharField(max_length=32, null=False)


class PartImage(models.Model):
    image = models.ImageField(upload_to='media/parts/%Y/%m/%d/')
    part = models.ForeignKey(to=Part, on_delete=models.CASCADE)
