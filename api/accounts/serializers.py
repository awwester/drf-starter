from rest_framework.serializers import ModelSerializer

from .models import User


class CustomUserSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
