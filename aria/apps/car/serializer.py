from rest_framework.serializers import ModelSerializer

from aria.apps.car.models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        optional_fields = ('user',)
        fields = ('manufacturer', 'car_type', 'models', 'year', )
