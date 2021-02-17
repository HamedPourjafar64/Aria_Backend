from aria.apps.aria_profile.views import AriaProfileCreate, AriaProfileDetail, AriaProfileUpdate
from django.urls import path


urlpatterns = [
    path('profile/detail/<int:pk>/', AriaProfileDetail.as_view(), name='part_detail'),
    path('profile/create/', AriaProfileCreate.as_view(), name='part_create'),
    path('profile/update/', AriaProfileUpdate.as_view(), name='part_update')
]
