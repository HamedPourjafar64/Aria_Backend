from django.urls import path

from aria.apps.contact.views import ContactList, ContactDetails

urlpatterns = [
    path('contact_list/', ContactList.as_view(), name='contact_list'),
    path('contact_details/', ContactDetails.as_view(), name='contact_details')
]
