from django.db import models
import uuid


class User(models.Model):
    user_id = models.CharField(max_length=128, default=uuid.uuid4, primary_key=True)
    login = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=128)

    def create_user(self):
        print(123)
