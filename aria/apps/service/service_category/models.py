from django.db import models


# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=64, null=False)
    image = models.ImageField(upload_to='/media/services/categories/%Y/%m/%d/', null=True)
