from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model


class UserCreateSerializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'name', 'password')