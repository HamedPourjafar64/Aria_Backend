from aria.apps.service.serializers import ServiceCreateUpdateSerializer


def create_service(service):
    serializer = ServiceCreateUpdateSerializer(data=service)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False