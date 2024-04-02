# f5rugby/views.py
# author: jose
# date: April 02, 2024

from django.http import HttpResponse
from django.shortcuts import render
import subprocess

def index(request):
    return render(request, 'f5rugby/index.html', context={})

def camps(request):
    return render(request, 'f5rugby/camps.html', context={})

def health(request):
    return render(request, 'f5rugby/health.html', context={})

def webhook_handler(request):
    if request.method == 'POST':
        # Execute git pull
        subprocess.Popen(['/home/reyesjl/django_sites/auto_update.sh'])
        return HttpResponse('Webhook received', status=200)
    else:
        return HttpResponse('Method not allowed', status=405)
