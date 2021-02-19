from aria.apps.user.logics import create_user
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def register_user(request):
    username = request.data['username']
    try:
        if create_user(username):
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(data={"message": "Wrong username value!"}, status=status.HTTP_400_BAD_REQUEST)
