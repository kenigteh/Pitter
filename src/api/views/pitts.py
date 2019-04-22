from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Pitt
from api.decorators import token_validation, login_validation


class Pitts(APIView):
    @staticmethod
    @token_validation
    @login_validation
    def post(request):
        audio_file = request.data.get('audio_file')
        audio_text = request.data.get('audio_text')

        if not audio_file or not audio_text or isinstance(audio_text, str):
            data = dict(error="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        user_id = request.current_app.get('user_id')

        Pitt.objects.create(user_id=user_id, audio_file=audio_file, audio_text=audio_text)
        data = dict(status="Success!")
        return Response(data=data, status=status.HTTP_201_CREATED)
