from aria.apps.aria_profile.models import AriaProfile
from rest_framework import generics, permissions
from aria.apps.aria_profile.serializers import AriaProfileSerializer, AriaProfileCreateUpdateSerializer


class AriaProfileDetail(generics.RetrieveAPIView):
    queryset = AriaProfile.objects.all()
    serializer_class = AriaProfileSerializer


class AriaProfileCreate(generics.CreateAPIView):
    queryset = AriaProfile.objects.all()
    serializer_class = AriaProfileCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class AriaProfileUpdate(generics.UpdateAPIView):
    queryset = AriaProfile.objects.all()
    serializer_class = AriaProfileSerializer