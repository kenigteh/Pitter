from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.serializers.user_serializer import UserSerializer


class UserManager(APIView):
    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = dict(status="Success!")
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

    @staticmethod
    def get(request):
        try:
            login = request.GET['login']
            user = User.objects.get(login=login)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        except Exception as e:
            data = dict(error=str(e))
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        login = request.current_app.get('user_login')
        try:
            user = User.objects.get(login=login)
        except ObjectDoesNotExist:
            data = dict(error="User to not found!")
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        user.delete()
        data = dict(status="Delete success!")
        return Response(data=data, status=status.HTTP_200_OK)
