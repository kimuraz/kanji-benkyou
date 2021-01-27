from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializers import UserSerializer


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def profile(request):
    """
    Returns or edits an user profile.
    """
    if request.method == 'GET':
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
    if request.method == 'PATCH':
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK) 
