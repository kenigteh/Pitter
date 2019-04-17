from django.conf.urls import url

from api import views

urlpatterns = [
    url('users/manager', views.UserManager.as_view()),
    url('users/search', views.UserManager.as_view()),
    url('auth', views.Authorization.as_view()),
]
