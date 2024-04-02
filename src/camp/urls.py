# camps/urls.py
from django.urls import path
from . import views

app_name = 'camps'
urlpatterns = [
    path('', views.index, name='index'),
]