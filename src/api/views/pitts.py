from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.constants import AUDIO_FORMAT
from api.decorators import token_validation, login_validation
from api.models import Pitt
from api.models import User


class Pitts(APIView):
    @staticmethod
    @token_validation
    @login_validation
    def post(request):
        audio_file = request.data.get('audio_file')
        audio_text = request.data.get('audio_text')

        if not audio_file or not audio_text or not isinstance(audio_text, str):
            data = dict(error="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(audio_file, InMemoryUploadedFile):
            data = dict(error="Bad file!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        audio_format = audio_file.name.split('.')[-1]
        if audio_format != AUDIO_FORMAT:
            data = dict(error="Bad file format!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        user_id = request.current_app.get('user_id')

        Pitt.objects.create(user_id=user_id, audio_file=audio_file, audio_text=audio_text)
        data = dict(status="Success!")
        return Response(data=data, status=status.HTTP_201_CREATED)

    @staticmethod
    @token_validation
    def get(request):
        login = request.data.get('login')

        if not login or not isinstance(login, str):
            data = dict(error="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_id = User.objects.get(login=login).user_id
        except ObjectDoesNotExist:
            data = dict(error="User to not found!")
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        pitts = list(Pitt.objects.filter(user_id=user_id).values_list('pitt_id', 'audio_file', 'audio_text', 'date'))
        data = dict(status="Success!", pitts=pitts)
        return JsonResponse(data=data, status=status.HTTP_200_OK)

    @staticmethod
    @token_validation
    def delete(request):
        pitt_id = request.data.get('pitt_id')

        if not pitt_id or not isinstance(pitt_id, str):
            data = dict(error="Bad request!")
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        try:
            pitt = Pitt.objects.get(pitt_id=pitt_id)
        except ObjectDoesNotExist:
            data = dict(error="Pitt not found!")
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        pitt.delete()
        data = dict(status="Success!")
        return Response(data=data, status=status.HTTP_200_OK)
