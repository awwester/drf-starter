from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
