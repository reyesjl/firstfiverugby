"""
URL configuration for f5rugby project.
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('camps/', views.camps, name='camps'),
    path('health/', views.health, name='health'),
    path('deploy-webhook/', views.webhook_handler, name='deploy_webhook'),
]
