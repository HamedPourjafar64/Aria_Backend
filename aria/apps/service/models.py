from django.db import models
from aria.apps.part.models import Part

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=256, null=True)
    image = models.ImageField(
        upload_to='media/services/%Y/%m/%d/', null=True, blank=True)
    price = models.BigIntegerField(null=False)
    category = models.ForeignKey(to='serviceCategory.ServiceCategory',
                                 on_delete=models.CASCADE)
    in_place = models.BooleanField(default=False)
    is_transfer = models.BooleanField(default=False)
    parts = models.ForeignKey(to=Part, on_delete=models.CASCADE)
    service_worker_fee = models.BigIntegerField(null=False)