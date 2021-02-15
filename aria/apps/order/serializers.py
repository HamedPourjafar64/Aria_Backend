from rest_framework import serializers
from datetime import datetime
from aria.apps.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 0

    def update(self, instance, validated_data):
        instance.updated_at = datetime.now()
        return super().update(instance, validated_data)
