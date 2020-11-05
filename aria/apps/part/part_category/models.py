from django.db import models


# Create your models here.
class PartCategory(models.Model):
    name = models.CharField(max_length=64, null=False)
    image = models.ImageField(upload_to='/media/parts/categories/%Y/%m/%d/')
