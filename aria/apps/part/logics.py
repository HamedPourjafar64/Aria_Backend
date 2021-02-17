

from aria.apps.part.serializers import PartSerializer


def create_part(part):
    serializer = PartSerializer(data=part)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False