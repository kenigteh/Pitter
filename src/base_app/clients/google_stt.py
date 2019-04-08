import base64

import json
import requests


def mp3_to_flac(audio):
    pass


def encode_audio(audio):
    audio_content = audio.read()
    return base64.b64encode(audio_content).decode('ascii')


def create_rec(audio_content):
    data = {
        'config': {
            'encoding': 'FLAC',
            'sampleRateHertz': 16000,
            'languageCode': 'ru-RU'
        },
        'audio': {
            'content': str(audio_content)
        }
    }
    return data


def send_req(data):
    key = 'AIzaSyAPgaSnLgDd0tIP_YxfKXBf59fNQ-IKocA'
    url = f"https://speech.googleapis.com/v1/speech:recognize?alt=json&key={key}"
    return requests.post(url, data=json.dumps(data)).json()


def speech_to_text(audio):
    data = encode_audio(audio)
    req_data = create_rec(data)
    print(send_req(req_data))


file = open("test.flac", "rb")
speech_to_text(file)
file.close()
