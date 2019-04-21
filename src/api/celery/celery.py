from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pitter.settings')
app = Celery('pitter')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
