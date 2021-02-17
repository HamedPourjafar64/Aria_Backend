from rest_framework import generics

from aria.apps.vehicle.models import Vehicle
from aria.apps.vehicle.serializer import VehicleCreateUpdateSerializer, VehicleSerializer


class VehicleList(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    # permission_classes = [permissions.IsAuthenticated]


class VehicleCreate(generics.CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleCreateUpdateSerializer

class VehicleUpdate(generics.UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleCreateUpdateSerializer

class VehicleDetail(generics.RetrieveDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    # permission_classes = [permissions.IsAuthenticated]
