from django.urls import path, include
from .views import home

app_name ='tt'

urlpatterns = [
    path( '', home, name='home' ),
]
