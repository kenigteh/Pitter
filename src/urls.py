from django.urls import path, include

urlpatterns = [
    path('base/', include('api.urls')),
]
