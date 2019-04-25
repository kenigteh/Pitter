from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def my_send_email(**kwargs):
    send_mail(**kwargs)
