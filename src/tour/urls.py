# tour/urls.py
from django.urls import path
from . import views

app_name = 'tour'
urlpatterns = [
    path('', views.index, name='index'),
    path('tour-quote/', views.tour_quote, name='tour_quote'),
]