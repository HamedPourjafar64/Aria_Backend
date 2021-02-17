from aria.apps.aria_address.serializers import AddressCreateUpdateSerializer, AddressSerializer
from aria.apps.aria_address.models import Address
from rest_framework import generics, permissions


class AddressList(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AddressDetail(generics.RetrieveDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AddressCreate(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressCreateUpdateSerializer


class AddressUpdate(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressCreateUpdateSerializer
