from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(GenericViewSet):
    """
    This is just a placeholder GenericViewSet to show structure of
    serializers.py file and allow adding a ViewSet through the router.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
