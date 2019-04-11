from rest_framework import serializers
from base_app.models.user import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('user_id', 'login', 'password', 'name', 'email', 'phone')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user