from django.urls import path

from aria.apps.user.views import authorize_user, register_user

urlpatterns = [
    path('user/auth/', register_user, name='authenticate_user'),
    path('user/auth/validate', authorize_user, name='authorize_user'),
]
