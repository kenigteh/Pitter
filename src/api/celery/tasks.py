from .celery import app
from django.core.mail import send_mail


@app.task
def my_send_email(**kwargs):
    send_mail(**kwargs)
