from django.conf.urls import url

from api import views

urlpatterns = [
    url('users/manager', views.UserManager.as_view()),
    url('users/search', views.UsersSearch.as_view()),
    url('subscriptions', views.SubManager.as_view()),
    url('auth', views.Authorization.as_view()),
]