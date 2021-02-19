from aria.apps.user.logics import authenticate_user, create_user, login_user
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def register_user(request):
    try:
        username = request.data['username']
        if authenticate_user(username):
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(data={"message": "Wrong username value!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def authorize_user(request):
    try:
        username = request.data['username']
        password = request.data['password']
        response = login_user(username=username, password=password)
        if hasattr(response, 'token'):
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={"message": "Wrong credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(data={"message": "Wrong credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
