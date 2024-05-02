# camps/urls.py
from django.urls import path
from . import views

app_name = 'camps'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:camp_id>/', views.details, name='details'),
    path('select-role/<int:camp_id>/', views.select_camp_role, name='select_camp_role'),
    path('register/<int:camp_id>/<str:register_type>/', views.register_stripe, name='register_new'),
    path('register-success/<path:payment_link>/', views.register_success, name='register_success'),
    path('edit-registration/<int:registration_id>/', views.edit_registration, name='edit_registration'),
    path('manager-panel/', views.manager_panel, name='manager_panel'),
    path('create/', views.create, name='create'),
]