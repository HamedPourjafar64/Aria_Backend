from rest_framework import serializers
from datetime import datetime
from aria.apps.order.models import Order

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('user',)
        depth = 1


    def update(self, instance, validated_data):
        instance.updated_at = datetime.now()
        return super().update(instance, validated_data)


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('user', )
        depth = 1

class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 0

    def to_representation(self, instance):
        ret = super(OrderCreateUpdateSerializer, self).to_representation(instance)
        ret.pop('user')
        return ret