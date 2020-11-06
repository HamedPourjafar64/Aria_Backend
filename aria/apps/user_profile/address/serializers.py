from rest_framework.serializers import ModelSerializer

from aria.apps.user_profile.address.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        optional_fields = ('user', 'country',)
        fields = (
            'city', 'district', 'street', 'apartment_no', 'pin_point_location', 'latitude', 'longitude',
        )
