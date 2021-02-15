from django.db import models
from django.conf import settings
from django.utils.timezone import now
from enum import IntEnum


class OrderStatus(IntEnum):
    # car types enum
    IN_PROGRESS = 1
    DONE = 2
    CANCELED = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]



class Order(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, related_name='user')
    service_worker = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='service_worker')
    services = models.ManyToManyField(to='service.Service', null=True, blank=True)
    src_addr = models.ForeignKey(
        to='aria_address.Address', on_delete=models.CASCADE, null=True, related_name='src_addr')
    dst_addr = models.ForeignKey(
        to='aria_address.Address', on_delete=models.CASCADE, null=True, related_name='dst_addr')
    
    order_time = models.DateTimeField(default=now, null=False)

    is_deleted = models.BooleanField(default=False)
    status = models.IntegerField(
        choices=OrderStatus.choices(),
        default=1,
        null=True
    )
    created_at = models.DateTimeField(editable=False, default=now)
    updated_at = models.DateTimeField(editable=False, default=now)
