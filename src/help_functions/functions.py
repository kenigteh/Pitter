import base64


def mp3_to_flac(audio):
    pass


def encode_audio(audio):
    audio_content = audio.read()
    return base64.b64encode(audio_content).decode("ascii")
