"""
URL configuration for f5rugby project.
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('camps/', include('camp.urls')),
    path('health/', include('health.urls')),
    path('tours/', include('tour.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('account.urls')),
    path('deploy-webhook/', views.webhook_handler, name='deploy_webhook'),
    path('success/', views.success_page, name='success_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
