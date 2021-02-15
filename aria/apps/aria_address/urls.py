from django.urls import path
from aria.apps.aria_address.views import *

urlpatterns = [
    path('address/list/', AddressList.as_view(), name='address_list'),
    path('address/detail/', AddressDetail.as_view(), name='address_detail'),
    path('address/validation/', address_validator)
]
