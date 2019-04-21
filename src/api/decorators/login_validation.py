from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response

from api.models import User


def login_validation(func):
    def wrapper(request):
        user_login = request.current_app.get('user_login')

        try:
            user_id = User.objects.get(login=user_login).user_id
        except ObjectDoesNotExist:
            data = dict(error="User login not found!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        request.current_app.update(dict(user_id=user_id))
        return func(request)

    return wrapper
