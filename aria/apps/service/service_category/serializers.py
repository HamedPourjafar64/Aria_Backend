from rest_framework.serializers import ModelSerializer

from aria.apps.service.service_category.models import ServiceCategory

class ServiceCategorySerializer(ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'
