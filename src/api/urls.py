from django.conf.urls import url

from api import views

urlpatterns = [
    url('upload_audio', views.UploadAudioFile.as_view()),
    url('user_manager', views.UserManager.as_view()),
    url('auth', views.Authorization.as_view()),
]
