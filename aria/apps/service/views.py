from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from aria.apps.service.models import Service
from aria.apps.service.serializers import ServiceCreateUpdateSerializer, ServiceSerializer


class ServiceList(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = [IsAuthenticated]

class ServiceCreate(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceCreateUpdateSerializer
    
class ServiceUpdate(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceCreateUpdateSerializer
    
class ServiceDetail(RetrieveDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = [IsAdminUser]
