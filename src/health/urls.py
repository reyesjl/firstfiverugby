# health/urls.py
from django.urls import path
from . import views

app_name = 'health'
urlpatterns = [
    path('', views.index, name='index'),
]