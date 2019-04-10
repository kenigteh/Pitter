from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from base_app.constants import rest_file_type
from integrations import google_stt
import uuid
from django.core.files.storage import FileSystemStorage
from base_app.constants import audio_files_path


class UserManager(APIView):
    def post(self, request):
        pass

    def get(self, request):
        pass
