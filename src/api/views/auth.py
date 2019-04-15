from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.user import User


class Authorization(APIView):
    def post(self, request):
        try:
            login = request.data.get('login')
            password = request.data.get('password')
        except KeyError:
            data = {"error": "No user password or login!"}
            return Response(data, status=400)

        user = User.objects.get(login=login, password=password)
        if not user:
            data = {"error": "Your login or password is incorrect"}
            return Response(data, status=400)

        data = {"status": user.name}
        return Response(data, status=200)

