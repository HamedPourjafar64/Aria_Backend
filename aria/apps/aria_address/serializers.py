from django.db.models import fields
from aria.apps.user.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer

from aria.apps.aria_address.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        optional_fields = ('country',) 
        exclude = ('user', )
        depth = 1

class AddressCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        depth = 0

    def to_representation(self, instance):
        ret = super(AddressCreateUpdateSerializer, self).to_representation(instance)
        ret.pop('user')
        return ret