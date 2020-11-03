from rest_framework import serializers
from django.conf import settings


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(max_length=128, allow_blank=True, allow_null=True, required=False)
    phone_no = serializers.CharField(max_length=32, allow_blank=True, allow_null=True, required=False)
    email = serializers.EmailField(max_length=128, allow_blank=True, allow_null=True, required=False)

    def to_representation(self, instance):
        ret = super(UserSerializer, self).to_representation(instance)
        ret.pop('password')
        return ret

    def create(self, validated_data):
        return settings.AUTH_USER_MODEL.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        return instance
