from aria.apps.user.logics import authenticate_user, user_validation
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def auth_user(request):
    username = request.data['username']
    if authenticate_user(username):
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(data={"message": "wrong or unaccepted phone number"},
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def validate_user(request):
    username = request.data['username']
    password = request.data['password']
    if user_validation(username, password).ok:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(data={"message": "wrong credentials!"},
                            status=status.HTTP_400_BAD_REQUEST)