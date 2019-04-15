import jwt
from rest_framework.response import Response
from rest_framework.views import APIView

from api.constants import secret
from api.models.user import User


class Authorization(APIView):
    def create_jwt(self, login):
        encoded_jwt = jwt.encode(
            {'login': login},
            str(secret),
            algorithm='RS256')
        return encoded_jwt

    def post(self, request):
        try:
            login = request.data['login']
            password = request.data['password']
        except KeyError:
            data = {"error": "No user password or login!"}
            return Response(data, status=400)

        user = User.objects.get(login=login, password=password)
        if not user:
            data = {"error": "Your login or password is incorrect"}
            return Response(data, status=401)

        data = {"key": self.create_jwt(login)}
        return Response(data, status=200)
