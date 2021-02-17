"""aria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('oauth2_provider.urls', namespace='token_provider')),
    path('', include('aria.apps.vehicle.urls')),
    path('', include('aria.apps.order.urls')),
    path('', include('aria.apps.aria_address.urls')),
    path('', include('aria.apps.service.urls')),
    path('', include('aria.apps.aria_profile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
