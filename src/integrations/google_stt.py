import requests
from base_app import constants
from help_functions import functions

REQ_DATA = constants.REQ_DATA


def create_rec(audio_content):
    data = {
        'config': {
            'encoding': REQ_DATA["encoding"],
            'languageCode': REQ_DATA["languageCode"]
        },
        'audio': {
            'content': audio_content
        }
    }
    return data


def send_req(data):
    return requests.post(constants.url, json=data, params={"key": constants.key}).json()


def speech_to_text(audio_file):
    data = functions.encode_audio(audio_file)
    req_data = create_rec(data)
    ans = send_req(req_data)
    if 'error' in ans:
        raise Exception(ans['error']['message'])
    return ans['results'][0]['alternatives'][0]['transcript']
