from aria.apps.aria_contact.serializers import ContactSerializer
from rest_framework import generics, permissions

# Create your views here.
from aria.apps.aria_contact.models import Contact


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
