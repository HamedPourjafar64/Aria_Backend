from django.db import models
from datetime import date, datetime, time
from django.contrib.auth.models import User
from enum import IntEnum

class OrderStatus(IntEnum):
    # car types enum
    IN_PROGRESS = 1
    DONE = 2
    CANCELED = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class OrderTime(models.Model):
    selected_day = models.DateField(default=date.today, null=False)
    selected_time = models.TimeField(default=time(), null=False)
    needs_asap = models.BooleanField(default=True, null=False)


class Order(models.Model):
    creation_date = models.DateTimeField(default=datetime.now, null=False)
    user = models.OneToOneRel(to=User, null=False, on_delete=models.CASCADE)
    service_worker = models.OneToOneRel(
        to=User, null=True, on_delete=models.CASCADE)
    services = models.ManyToManyField(to='service.Service')
    src_addr = models.OneToOneRel(
        to='address.Address', on_delete=models.CASCADE)
    dst_addr = models.OneToOneRel(
        to='address.Address', on_delete=models.CASCADE)
    order_time = models.OneToOneRel(to=OrderTime, on_delete=models.CASCADE)
    priority = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    status = models.IntegerField(
        choices=OrderStatus.choices(),
        default=1,
        null=True
    )