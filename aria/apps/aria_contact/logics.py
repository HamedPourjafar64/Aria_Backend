

from aria.apps.aria_contact.serializers import ContactCreateUpdateSerializer


def create_contact(contact):
    serializer = ContactCreateUpdateSerializer(data=contact)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False


