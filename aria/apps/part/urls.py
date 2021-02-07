from django.urls import path

from aria.apps.part.views import PartDetail, PartList, PartCreation

urlpatterns = [
    path('part/list/', PartList.as_view(), name='part_list'),
    path('part/detail/', PartDetail.as_view(), name='part_detail'),
    path('part/create/', PartCreation.as_view(), name='part_create')
]
