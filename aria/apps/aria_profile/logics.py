from django.contrib.auth.models import User
from aria.apps.aria_profile.serializers import AriaProfileCreateUpdateTestSerializer
from aria.apps.aria_profile.models import AriaProfile

def create_profile(profile, username):
    profile['user'] = get_user_id(username=username)
    serializer = AriaProfileCreateUpdateTestSerializer(data= profile)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False

def update_profile(profile: AriaProfile, new_version, username):
    new_version['user'] = get_user_id(username=username)
    serializer = AriaProfileCreateUpdateTestSerializer(profile, data=new_version)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False

def get_user_id(username):
    user = User.objects.get(username=username)
    return user.id