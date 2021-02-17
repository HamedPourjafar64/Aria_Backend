


from aria.apps.service.service_category.serializers import ServiceCategorySerializer


def create_service_category(service_category):
    serializer = ServiceCategorySerializer(data=service_category)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False