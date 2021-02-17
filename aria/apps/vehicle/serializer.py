from attr import field
from aria.apps.user.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from aria.apps.vehicle.models import Vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        depth = 1

class VehicleCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        depth = 0

