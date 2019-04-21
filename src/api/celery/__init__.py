from .celery import app as celery_app
from .tasks import my_send_email


__all__ = (
    'celery_app',
    'my_send_email',
)
