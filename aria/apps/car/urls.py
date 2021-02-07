from django.urls import path

from aria.apps.car.views import CarList, CarDetail

urlpatterns = [
    path('car/list/', CarList.as_view(), name='car_list'),
    path('car/detail/', CarDetail.as_view(), name='car_detail')
]
