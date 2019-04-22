# Данные здесь на время разработки. Заменю на переменные окружения в конце разработки.

key = 'AIzaSyAPgaSnLgDd0tIP_YxfKXBf59fNQ-IKocA'
url = f"https://speech.googleapis.com/v1/speech:recognize?alt=json&key={key}"

REQ_DATA = {
    "encoding": "FLAC",
    "languageCode": "ru-RU"
}

rest_file_type = "<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>"

audio_files_path = "media/audio-files"

with open("files/secret.txt") as f:
    secret = f.read()

with open("files/public_key.txt") as f:
    public_key = f.read()
