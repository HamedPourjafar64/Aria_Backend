from django.contrib.auth.models import User



from aria.apps.order.models import Order
from aria.apps.order.serializers import OrderCreateUpdateSerializer


def validate_order(order:Order):
    serializer = OrderCreateUpdateSerializer(data=order)
    if serializer.is_valid(raise_exception=True):
        return True
    raise ValueError('Order object is wrong!')


def get_current_user_id(username):
    user = User.objects.get(username=username)
    return user.id

def create(order:Order):
    serializer = OrderCreateUpdateSerializer(data=order)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False 