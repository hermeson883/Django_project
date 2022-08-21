from django.urls import path
from django_anuncios.views import home

urlpatterns =[
    path("", home, name='home'),
]