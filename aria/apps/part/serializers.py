from rest_framework import serializers

from aria.apps.part.models import Part


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part