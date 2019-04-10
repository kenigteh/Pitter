from django.conf.urls import url

from base_app import views

urlpatterns = [
    url('health', views.HeartBeatHealthCheck.as_view()),
    url('upload_audio', views.UploadAudioFile.as_view()),
]
