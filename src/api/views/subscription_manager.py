from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Subscription
from api.models import User
from api.my_functions import my_send_email
from api.decorators import token_validation


class SubManager(APIView):
    @staticmethod
    @token_validation
    def put(request):
        token = request.data.get("token")
        user_to = request.data.get("user_to")

        if not token or not user_to:
            data = dict(error="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        token = decode_token(token)
        if not token:
            data = dict(error="Bad token!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        user_from = token.get('login')
        try:
            user_from_id = User.objects.get(login=user_from).user_id
        except ObjectDoesNotExist:
            data = dict(error="User from not found!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_to_id = User.objects.get(login=user_to).user_id
        except ObjectDoesNotExist:
            data = dict(error="User to not found!")
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            Subscription.objects.create(user_from=user_from_id, user_to=user_to_id)
        except:
            data = dict(error="Can't save subscription.")
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        my_send_email(subject="На вас подписались!",
                      message=f"Пользователь {user_to} подписался на вас в Питтере!",
                      from_email='Pitter@ferf.com',
                      recipient_list=['artemon1002@mail.ru'])

        data = dict(status="Success!")
        return Response(data=data, status=status.HTTP_201_CREATED)

    @staticmethod
    @token_validation
    def get(request):
        user_login = request.current_app.get('user_login')
        try:
            user_id = User.objects.get(login=user_login).user_id
        except ObjectDoesNotExist:
            data = dict(error="User login not found!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        try:
            subs = Subscription.objects.filter(user_from=user_id)
            logins = []
            for sub in subs:
                user_to_id = sub.user_to
                try:
                    login = User.objects.get(user_id=user_to_id).login
                    logins.append(login)
                except:
                    continue
        except ObjectDoesNotExist:
            data = dict(error="User login not found!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        data = dict(error="Success!", data=logins)
        return Response(data=data, status=status.HTTP_200_OK)

    @staticmethod
    @token_validation
    def delete(request):
        token = request.data.get("token")
        user_to = request.data.get("user_to")

        if not token or not user_to:
            data = dict(error="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        token = decode_token(token)
        if not token:
            data = dict(error="Bad token!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        user_login = token.get('login')

        try:
            user_from_id = User.objects.get(login=user_login).user_id
        except ObjectDoesNotExist:
            data = dict(error="User login not found!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_to_id = User.objects.get(login=user_to).user_id
        except ObjectDoesNotExist:
            data = dict(error="User unsub login not found!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        try:
            Subscription.objects.filter(user_from=user_from_id, user_to=user_to_id).delete()
        except:
            data = dict(error="Can't delete subscription.")
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        data = dict(status="Success!")
        return Response(data=data, status=status.HTTP_200_OK)
