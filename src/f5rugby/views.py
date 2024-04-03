# f5rugby/views.py
# author: jose
# date: April 02, 2024

import logging
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from camp.models import Camp

# Configure logging
logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'f5rugby/index.html', context={})

def camps(request):
    all_camps = Camp.objects.order_by('start_date')
    context = {'camps': all_camps}

    return render(request, 'f5rugby/camps.html', context)

def health(request):
    return render(request, 'f5rugby/health.html', context={})

def success_page(request):
    return render(request, 'f5rugby/success_page.html')

@csrf_exempt
def webhook_handler(request):
    if request.method == 'POST':
        logger.info('Webhook received')
        try:
            # Execute git pull
            subprocess.Popen(['/home/reyesjl/django_sites/auto_update.sh'])
            logger.info('Git pull command executed')
        except Exception as e:
            logger.error('Error executing git pull command: %s' % str(e))
            return HttpResponse('Error executing git pull command', status=500)
        
        return HttpResponse('Webhook received', status=200)
    else:
        logger.warning('Method not allowed')
        return HttpResponse('Method not allowed', status=405)
