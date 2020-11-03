from django.urls import path
from aria.apps.person_assets.views import address_view

urlpatterns = [
    path('address_list/', address_view.AddressList.as_view(), name='address_list'),
    path('address_detail', address_view.AddressDetail.as_view(), name='address_detail')
]
