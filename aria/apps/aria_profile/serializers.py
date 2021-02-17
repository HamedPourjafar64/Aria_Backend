from aria.apps.aria_profile.models import AriaProfile
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault 
from django.contrib.auth.models import User

class AriaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AriaProfile
        exclude = ('user', )
        depth = 1


class AriaProfileCreateUpdateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(default=CurrentUserDefault())
    class Meta:
        model = AriaProfile
        fields = '__all__'
        depth = 0


    def to_representation(self, instance):
        ret = super(AriaProfileCreateUpdateSerializer,
                    self).to_representation(instance)
        ret.pop('user')
        return ret
