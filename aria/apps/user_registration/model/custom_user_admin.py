from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from aria.apps.user_registration.settings import UserRegistrationSettings as Settings


class CustomUserAdmin(UserAdmin):
    model = settings.AUTH_USER_MODEL
    list_display = ()  # Contain only fields in your `custom-user-models`
    list_filter = ()  # Contain only fields in your `custom-user-models` intended for filtering. Do not include
    # `groups`since you do not have it
    search_fields = ()  # Contain only fields in your `custom-user-models` intended for searching
    ordering = ()  # Contain only fields in your `custom-user-models` intended to ordering
    filter_horizontal = ()  # Leave it empty. You have neither `groups` or `user_permissions`
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number' if Settings.USER_NAME_FIELD == 'phone_number' else 'email',)}),
    )
