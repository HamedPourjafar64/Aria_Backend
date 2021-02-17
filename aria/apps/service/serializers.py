from rest_framework.serializers import ModelSerializer

from aria.apps.service.models import Service

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        depth = 1


class ServiceCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        depth = 0