from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from base_app.serializers.user_serializer import UserSerializer


class UserManager(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"status": "Success!"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

    def get(self, request):
        pass
