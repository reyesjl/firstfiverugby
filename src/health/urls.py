# health/urls.py
from django.urls import path
from . import views

app_name = 'health'
urlpatterns = [
    path('', views.index, name='index'),
    path('fitness-evaluation/', views.submit_fitness_evaluation, name='fitness_evaluation'),
]