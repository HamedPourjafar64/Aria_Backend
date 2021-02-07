from django.urls import path

from aria.apps.service.service_category.views import ServiceCategoryDetail, ServiceCategoryList, ServiceCategoryCreate

urlpatterns = [
    path('service/category/list/', ServiceCategoryList.as_view(), name='service_category_list'),
    path('service/category/detail/', ServiceCategoryDetail.as_view(), name='service_category_detail'),
    path('service/category/create/', ServiceCategoryCreate.as_view(), name='service_category_create')
]
