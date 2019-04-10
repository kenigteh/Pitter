from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from base_app.constants import rest_file_type
from integrations import google_stt
import uuid
from django.core.files.storage import FileSystemStorage


class UploadAudioFile(APIView):
    def post(self, request, format=None):
        if 'audio_file' not in request.data:
            data = {"status": "File key not correctly transmitted"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        audio_file = request.data.get('audio_file')

        if str(type(audio_file)) != rest_file_type:
            data = {"status": "You did not transfer the file"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        audio_type = str(audio_file).split('.')[-1]
        if audio_type != 'flac':
            data = {"status": "The extension of your file is not .flac"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Пытаемся сохранить:
        audio_file_name = str(uuid.uuid4())
        try:
            fs = FileSystemStorage(location='/media/audios')
            fs.save(audio_file_name, audio_file)
            audio_file = fs.open(audio_file_name)
        except Exception as e:
            data = {"status": str(e)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # Пытаемся транскрибировать файл:
        try:
            audio_text = google_stt.speech_to_text(audio_file)
            data = {"status": audio_text}
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            fs = FileSystemStorage(location='/media/audios')
            fs.delete(audio_file_name)
            data = {"status": str(e)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
