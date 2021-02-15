from aria.apps.aria_profile.serializers import AriaProfileSerializer
from aria.apps.aria_profile.models import AriaProfile

def create_profile(profile):
    serializer = AriaProfileSerializer(data= profile)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False

def update_profile(profile: AriaProfile, new_version):
    serializer = AriaProfileSerializer(profile, data=new_version)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False