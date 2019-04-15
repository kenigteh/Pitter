import uuid
from datetime import datetime

from django.db import models


class Wall(models.Model):
    wall_id = models.CharField(max_length=128, default=uuid.uuid4, primary_key=True)
    user_id = models.CharField(max_length=128)
    pitt_id = models.CharField(max_length=128)
    comment = models.CharField(max_length=128)
    date = models.DateTimeField(default=datetime.now)
