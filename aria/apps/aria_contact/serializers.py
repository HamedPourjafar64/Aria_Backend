from rest_framework import serializers

from aria.apps.aria_contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ('profile', )
        depth = 1


class ContactCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        depth = 0

    def to_representation(self, instance):
        ret = super(ContactCreateUpdateSerializer,
                    self).to_representation(instance)
        ret.pop('profile')
        return ret
