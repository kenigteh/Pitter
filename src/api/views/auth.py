import jwt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.constants import secret
from api.models import User


class Authorization(APIView):
    @staticmethod
    def create_jwt(login):
        encoded_jwt = jwt.encode(
            dict(login=login),
            str(secret),
            algorithm='RS256')
        return encoded_jwt

    def post(self, request):
        login = request.data.get('login', False)
        password = request.data.get('password', False)
        if not login or not password:
            data = dict(error="Bad request!")
            return Response(data, status=400)

        try:
            user = User.objects.get(login=login, password=password)
        except ObjectDoesNotExist:
            data = dict(error="Your login or password is incorrect")
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

        if not user:
            data = dict(error="User not found!")
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        data = dict(key=self.create_jwt(login))
        return Response(data, status=200)
