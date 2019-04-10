from django.urls import path, include

urlpatterns = [
    path('base/', include('base_app.urls')),
]
