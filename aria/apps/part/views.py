from rest_framework import generics, permissions

from aria.apps.part.models import Part
from aria.apps.part.serializers import PartSerializer


class PartList(generics.ListAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [permissions.IsAuthenticated]


class PartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [permissions.IsAdminUser]

class PartCreation(generics.CreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [permissions.IsAdminUser]
