from aria.apps.aria_contact.serializers import ContactCreateUpdateSerializer, ContactSerializer
from rest_framework import generics, permissions

# Create your views here.
from aria.apps.aria_contact.models import Contact


class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContactUpdate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]



class ContactDetails(generics.RetrieveDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
