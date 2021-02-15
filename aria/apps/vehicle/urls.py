from django.urls import path

from aria.apps.vehicle.views import VehicleDetail, VehicleList

urlpatterns = [
    path('vehicle/list/', VehicleList.as_view(), name='vehicle_list'),
    path('vehicle/detail/', VehicleDetail.as_view(), name='vehicle_detail'),
]
