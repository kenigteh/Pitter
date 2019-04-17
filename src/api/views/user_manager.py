from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.my_functions import decode_token
from api.serializers.user_serializer import UserSerializer


class UserManager(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"status": "Success!"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

    def get(self, request):
        try:
            login = request.GET['login']
            print(login)
            user = User.objects.get(login=login)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        except Exception as e:
            data = {"error": str(e)}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            token = request.data.get("token")
            token = decode_token(token)
            login = token.get("login")
            user = User.objects.get(login=login)
            user.delete()
            data = {"status": "Delete success!"}
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {"error": str(e)}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
