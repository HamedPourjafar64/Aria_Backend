from rest_framework import serializers

from aria.apps.aria_contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        depth = 1
