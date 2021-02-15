from django.urls import path

from aria.apps.aria_contact.views import ContactList, ContactDetails

urlpatterns = [
    path('contact/list/', ContactList.as_view(), name='contact_list'),
    path('contact/details/', ContactDetails.as_view(), name='contact_details')
]
