from django.db import models


# Create your models here.
class DetailedReceipt(models.Model):
    """
    this is for mostly company usage of the receipt cause they might need a more detailed
    usages of parts or services that have been done or maybe they just want to look at the
    details of final price.
    """
    item_name = models.CharField(null=False, max_length=128)
    item_price = models.BigIntegerField(null=False)
    receipt_id = models.ForeignKey(to='receipt.Receipt', on_delete=models.CASCADE)
