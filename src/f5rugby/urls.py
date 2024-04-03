"""
URL configuration for f5rugby project.
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('camps/', include('camp.urls')),
    path('health/', include('health.urls')),
    path('deploy-webhook/', views.webhook_handler, name='deploy_webhook'),
    path('success/', views.success_page, name='success_page'),
]
