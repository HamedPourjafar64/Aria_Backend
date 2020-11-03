from django.contrib import admin
# Register your models here.
from aria.apps.user_registration.model.custom_user_admin import CustomUserAdmin
from aria.apps.user_registration.model.user import User

admin.site.register(User, CustomUserAdmin)
