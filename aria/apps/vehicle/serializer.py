from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from aria.apps.vehicle.models import Vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        depth = 0

    def create(self, validated_data):
        return super().create(validated_data)
