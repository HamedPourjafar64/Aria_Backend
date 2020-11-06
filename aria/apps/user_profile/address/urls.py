from django.urls import path

from aria.apps.user_profile.address.views import AddressList, AddressDetail

urlpatterns = [
    path('address_list/', AddressList.as_view(), name='address_list'),
    path('address_detail', AddressDetail.as_view(), name='address_detail')
]
