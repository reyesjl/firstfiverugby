# f5rugby/views.py
# author: jose
# date: April 02, 2024

import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'f5rugby/index.html', context={})

def camps(request):
    return render(request, 'f5rugby/camps.html', context={})

def health(request):
    return render(request, 'f5rugby/health.html', context={})

@csrf_exempt
def webhook_handler(request):
    if request.method == 'POST':
        # Execute git pull
        subprocess.Popen(['/home/reyesjl/django_sites/auto_update.sh'])
        return HttpResponse('Webhook received', status=200)
    else:
        return HttpResponse('Method not allowed', status=405)
