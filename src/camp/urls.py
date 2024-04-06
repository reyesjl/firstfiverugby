# camps/urls.py
from django.urls import path
from . import views

app_name = 'camps'
urlpatterns = [
    path('', views.index, name='index'),
    path('select-role/', views.select_camp_role, name='select_camp_role'),
    path('register/', views.register_for_camp, name='register'),
    path('coach-register/', views.register_for_camp_as_coach, name='register_coach')
]