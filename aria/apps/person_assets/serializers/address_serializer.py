from rest_framework.serializers import ModelSerializer
from aria.apps.person_assets.model.address import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        optional_fields = ('user', 'country',)
        fields = (
            'city', 'district', 'street', 'apartment_no', 'pin_point_location', 'latitude', 'longitude',
        )
