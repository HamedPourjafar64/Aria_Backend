from aria.apps.aria_profile.models import AriaProfile
from rest_framework import serializers


class AriaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AriaProfile
        fields = '__all__'