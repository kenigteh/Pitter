from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.my_functions import decode_token


class UsersSearch(APIView):
    @staticmethod
    def post(request):
        token = request.data.get("token")
        logins = request.data.get("logins")

        if not token or logins is None or not isinstance(logins, list):
            data = dict(error="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        token = decode_token(token)
        if not token:
            data = dict(error="Bad token!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        if logins:
            users = User.objects.filter(login__in=logins)
        else:
            users = User.objects.all()

        data = list()
        for user in users:
            try:
                data.append(dict(
                    login=user.login,
                    name=user.name
                ))
            except:
                continue
        resp_data = dict(status="Success!", data=data)
        return Response(data=resp_data, status=status.HTTP_200_OK)

    @staticmethod
    def get(request):
        token = request.data.get("token")
        login = request.data.get("login")

        if not token or not login or not isinstance(login, str):
            data = dict(status="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        token = decode_token(token)
        if not token:
            data = dict(error="Bad token!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        users = User.objects.filter(login__icontains=login)
        data = list()
        for user in users:
            try:
                data.append(dict(
                    login=user.login,
                    name=user.name
                ))
            except:
                continue
        resp_data = dict(status="Success!", data=data)
        return Response(data=resp_data, status=status.HTTP_200_OK)
