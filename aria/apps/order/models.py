from django.db import models
from datetime import datetime
from django.conf import settings


# Create your models here.
class Order(models.Model):
    creation_date = models.DateTimeField(default=datetime.now, null=False)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=False, on_delete=models.SET_NULL)
    service_worker = models.ForeignKey(to='service_worker.ServiceWorker', null=True,
                                       on_delete=models.SET_NULL)
    parts = models.ManyToManyField(to='part.Part')
    services = models.ManyToManyField(to='service.Service')
