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

    @staticmethod
    def post(self, request):
        try:
            login = request.data['login']
            password = request.data['password']
        except KeyError:
            data = dict(error="No user password or login!")
            return Response(data, status=400)

        try:
            user = User.objects.get(login=login, password=password)
        except ObjectDoesNotExist:
            data = dict(error="User not found!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        if not user:
            data = dict(error="Your login or password is incorrect")
            return Response(data, status=401)

        data = dict(key=self.create_jwt(login))
        return Response(data, status=200)
