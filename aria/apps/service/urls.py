from django.urls import path

from aria.apps.service.views import ServiceDetail, ServiceList, ServiceCreate

urlpatterns = [
    path('service/list/', ServiceList.as_view(), name='service_list'),
    path('service/detail/', ServiceDetail.as_view(), name='service_detail'),
    path('service/create/', ServiceCreate.as_view(), name='service_create')
]
