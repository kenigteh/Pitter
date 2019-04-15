from django.conf.urls import url

from api import views

urlpatterns = [
    url('user_manager', views.UserManager.as_view()),
    url('auth', views.Authorization.as_view()),
]
