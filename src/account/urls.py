from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.logon, name='login'),
    path('logout/', views.logoff, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('camps/admin/', views.camps_admin, name='camps_admin')
]