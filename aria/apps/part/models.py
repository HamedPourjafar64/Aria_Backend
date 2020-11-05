from django.db import models


# Create your models here.
class Part(models.Model):
    name = models.CharField(max_length=64, null=False)
    brand_name = models.CharField(max_length=64)
    category = models.ForeignKey(to='aria.apps.part.part_category.PartCategory', on_delete=models.CASCADE)
    price = models.BigIntegerField(null=True)


class PartImage(models.Model):
    image = models.ImageField(upload_to='/media/parts/%Y/%m/%d/')
    part = models.ForeignKey(to=Part, on_delete=models.CASCADE)