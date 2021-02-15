from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import Serializer


from aria.apps.order.models import Order
from aria.apps.order.serializers import OrderSerializer


def validate_order(order:Order):
    serializer = OrderSerializer(data=order)
    if serializer.is_valid(raise_exception=True):
        return True
    raise ValueError('Order object is wrong!')


def get_current_user_id(username):
    user = User.objects.get(username=username)
    return user.id

def create(order:Order):
    serializer = OrderSerializer(data=order)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False 