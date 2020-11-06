from django.db import models
from enum import IntEnum
from datetime import datetime


class PaymentStatus(IntEnum):
    UNPAID = 1
    COMPANY_PAYMENT = 2
    PAID = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class PaymentMethod(IntEnum):
    COMPANY_CONTRACT = 1
    ONLINE = 2
    IN_PERSON = 3
    NONE = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


# Create your models here.
class Receipt(models.Model):
    """
    cause in receipt we have a foreign key to order we put receipt inside the order app
    """
    discount = models.BigIntegerField(null=True)
    total_price = models.BigIntegerField(null=False)
    payment_status = models.IntegerField(choices=PaymentStatus.choices(), default=PaymentStatus.UNPAID)
    payment_method = models.IntegerField(choices=PaymentMethod.choices(), default=PaymentMethod.NONE)
    payment_date = models.DateTimeField(default=datetime.now, null=False)
    order_id = models.ForeignKey(to='order.Order', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=datetime.now, null=False)
