from django.db import models


# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=64, null=True)
    image = models.ImageField(upload_to='services/categories/%Y/%m/%d/', null=False,)
    enabled = models.BooleanField(default=False)