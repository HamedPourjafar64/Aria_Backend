from rest_framework.serializers import ModelSerializer

from aria.apps.aria_address.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        optional_fields = ('user', 'country',)
        fields = '__all__'
