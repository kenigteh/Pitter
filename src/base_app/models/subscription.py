from django.db import models
import uuid


class Subscription(models.Model):
    sub_id = models.CharField(max_length=128, default=uuid.uuid4, primary_key=True)
    user_from = models.CharField(max_length=128)
    user_to = models.CharField(max_length=128)
