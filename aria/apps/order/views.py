from aria.apps.order.serializers import OrderListSerializer, OrderCreateUpdateSerializer
from aria.apps.order.models import Order
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer

class OrderUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer