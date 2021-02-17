from aria.apps.aria_address.serializers import AddressCreateUpdateSerializer

def create_address(address):
    serializer = AddressCreateUpdateSerializer(data=address)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False