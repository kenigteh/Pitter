import base64

import json
import requests
from base_app import constants

REQ_DATA = constants.REQ_DATA


def mp3_to_flac(audio):
    pass


def encode_audio(audio):
    audio_content = audio.read()
    return base64.b64encode(audio_content).decode("ascii")


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
    return requests.post(constants.url, json=data, params={"key": constants.key}).text


def speech_to_text(audio_path):
    data = encode_audio(audio_path)
    req_data = create_rec(data)
    print(send_req(req_data))


f = open("qwerty.flac", "rb")
speech_to_text(f)

f.close()
