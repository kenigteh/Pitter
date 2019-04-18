import os

import jwt
from celery import Celery
from celery import task
from django.core.mail import send_mail

from .constants import public_key

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pitter.src.settings')

app = Celery('Pitter')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


def decode_token(encoded_token):
    try:
        data = jwt.decode(encoded_token, public_key, algorithms='RS256')
        return data
    except:
        return None


@app.task
def my_send_email(**kwargs):
    send_mail(**kwargs)