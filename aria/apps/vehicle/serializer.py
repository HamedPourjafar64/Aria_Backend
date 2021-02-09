from rest_framework.serializers import ModelSerializer

from aria.apps.vehicle.models import Car


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
