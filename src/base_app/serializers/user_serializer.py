from rest_framework import serializers
from base_app.models.user import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('user_id', 'login', 'password', 'name', 'email', 'phone')
