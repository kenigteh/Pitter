from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.decorators import token_validation, login_validation
from api.models import Pitt
from api.models import Subscription
from api.models import User


class Wall(APIView):
    @staticmethod
    @token_validation
    @login_validation
    def post(request):
        offset = request.data.get('offset', '0')
        if not offset or not isinstance(offset, str) and not offset.isdiggit():
            data = dict(error='Bad offset')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        user_id = request.current_app.get('user_id')

        subs = Subscription.objects.filter(user_from=user_id)
        users_to_ids = [i.user_to for i in subs]
        wall_data = []
        for user_id in users_to_ids:
            try:
                login = User.objects.get(user_id=user_id).login
                pitts = Pitt.objects.filter(user_id=user_id)
                if pitts:
                    my_pitts = list()
                    for pitt in pitts:
                        my_pitts.append(dict(
                            pitt_id=pitt.pitt_id,
                            login=login,
                            text=pitt.audio_text,
                            audio=pitt.audio_file.url,
                            date=pitt.date
                        ))
                    wall_data.extend(my_pitts)
            except ObjectDoesNotExist:
                continue

        wall_data.sort(key=lambda pitt: pitt.get('date'), reverse=True)

        offset = abs(int(offset))
        wall_data = wall_data[offset:offset + 30]

        data = dict(status='Succes',
                    data=wall_data)
        return Response(data, status=status.HTTP_200_OK)
