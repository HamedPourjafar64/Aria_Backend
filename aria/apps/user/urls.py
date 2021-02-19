from django.urls import path

from aria.apps.user.views import register_user

urlpatterns = [
    path('user/auth/', register_user, name='create_user'),
]
