import uuid
from datetime import datetime

from django.db import models


class Pitt(models.Model):
    pitt_id = models.CharField(max_length=128, default=uuid.uuid4, primary_key=True)
    user_id = models.CharField(max_length=128)
    audio_file_name = models.FilePathField(max_length=128)
    audio_text = models.CharField(max_length=128)
    date = models.DateTimeField(default=datetime.now)
