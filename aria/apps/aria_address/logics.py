from aria.apps.aria_address.serializers import AddressSerializer


def check_support_zone(support_zone, address):
    validate_address(address=address)


def validate_address(address):
    serializer = AddressSerializer(data=address)
    if serializer.is_valid(raise_exception=True):
        return True
    return False

def create_address(address):
    serializer = AddressSerializer(data=address)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False