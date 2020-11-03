from django.urls import path
from aria.apps.person_assets.views import car_view

urlpatterns = [
    path('car_list/', car_view.CarList.as_view(), name='car_list'),
    path('car_detail/', car_view.CarDetail.as_view(), name='car_detail')
]