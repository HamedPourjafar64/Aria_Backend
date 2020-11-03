from django.urls import path
from aria.apps.user_registration.views import views

urlpatterns = [
    path('register/', views.register),
    path('validate/', views.validate),
]
