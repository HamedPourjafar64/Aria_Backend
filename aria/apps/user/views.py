from django.views.decorators.csrf import csrf_exempt
from aria.apps.user.logics import create_user
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def register_user(request):
    # first we need to check if user exist or not if it exist we need to send a notification message and check if user is assigned to group
    username = request.data['username']
    try:
        if create_user(username):
            return Response(status=status.HTTP_204_NO_CONTENT)
    except ValueError:
        return Response({
            'status' : status.HTTP_400_BAD_REQUEST,
            'message' : ValueError
        })