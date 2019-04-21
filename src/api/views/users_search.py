from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.decorators import token_validation
from api.models import User


class UsersSearch(APIView):
    @staticmethod
    @token_validation
    def post(request):
        logins = request.data.get("logins")

        if logins is None or not isinstance(logins, list):
            data = dict(error="Bad request!")
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
            except KeyError:
                continue
        resp_data = dict(status="Success!", data=data)
        return Response(data=resp_data, status=status.HTTP_200_OK)

    @staticmethod
    @token_validation
    def get(request):
        login = request.data.get("login")

        if not login or not isinstance(login, str):
            data = dict(status="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        users = User.objects.filter(login__icontains=login)
        data = list()
        for user in users:
            try:
                data.append(dict(
                    login=user.login,
                    name=user.name
                ))
            except KeyError:
                continue
        resp_data = dict(status="Success!", data=data)
        return Response(data=resp_data, status=status.HTTP_200_OK)
