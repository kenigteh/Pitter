import jwt
from rest_framework import status
from rest_framework.response import Response

from api.constants import public_key


def decode_token(encoded_token):
    try:
        data = jwt.decode(encoded_token, public_key, algorithms='RS256')
        return data
    except (jwt.exceptions.InvalidSignatureError, jwt.exceptions.DecodeError):
        return None


def token_validation(func):
    def wrapper(request):
        print(request.query_params)
        token = request.data.get("token")
        if not token:
            data = dict(error="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        token = decode_token(token)
        if not token:
            data = dict(error="Bad token!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        user_login = token.get('login')
        request.current_app = dict(user_login=user_login)
        return func(request)

    return wrapper
