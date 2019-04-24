from django.conf.urls import url

from api import views

urlpatterns = [
    url('users/manager', views.UserManager.as_view()),
    url('users/search', views.UsersSearch.as_view()),
    url('users/subscriptions', views.SubManager.as_view()),
    url('users/auth', views.Authorization.as_view()),
    url('pitts', views.Pitts.as_view()),
    url('wall', views.Wall.as_view()),
]
