from django.urls import path

from aria.apps.user.views import auth_user, validate_user

urlpatterns = [
    path('user/auth/', auth_user, name='authenticate_user'),
    path('user/auth/validate', validate_user, name='authorize_user'),
]
