import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Subscription(models.Model):
    sub_id = models.CharField(max_length=128, default=uuid.uuid4, primary_key=True)
    user_from = models.CharField(max_length=128, null=False)
    user_to = models.CharField(max_length=128, null=False)

    @classmethod
    def validate_unique(*cls, **kwargs):
        user_from = kwargs.get('user_from', False)
        user_to = kwargs.get('user_to', False)
        if not user_from or not user_to:
            return False
        try:
            Subscription.objects.get(user_from=user_from,
                                     user_to=user_to)
            return False
        except ObjectDoesNotExist:
            return True
