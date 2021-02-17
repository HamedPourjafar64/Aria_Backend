from django.urls import path

from aria.apps.order.views import OrderCreate, OrderList

urlpatterns = [
    path('order/list/', OrderList.as_view(), name='order_list'),
    path('order/create/', OrderCreate.as_view(), name='order_create'),
]
