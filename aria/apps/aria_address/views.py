from aria.apps.aria_address.serializers import AddressSerializer
from aria.apps.aria_address.models import Address
from aria.apps.aria_address.logics import  validate_address
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes





class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]



@api_view
@permission_classes([permissions.IsAuthenticated])
def check_address_zone(request):
    support_zone = request.data['support_zone']
    address = request.data['address']
    

@api_view
def address_validator(request):
    if validate_address(request.data):
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)