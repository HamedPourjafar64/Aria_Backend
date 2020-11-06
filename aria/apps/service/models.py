from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=256, null=True)
    image = models.ImageField(upload_to='/media/services/%Y/%m/%d/', null=True, blank=True)
    starting_price = models.BigIntegerField(null=False)
    category = models.ForeignKey(to='serviceCategory.ServiceCategory',
                                 on_delete=models.CASCADE)
