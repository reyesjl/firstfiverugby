# f5rugby/views.py
# author: jose
# date: April 02, 2024

import os
import hmac
import hashlib
from dotenv import load_dotenv
import logging
import subprocess
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from camp.models import Camp

# Configure logging
logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'f5rugby/index-new.html', context={})

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
    load_dotenv()
    GITHUB_SECRET = os.getenv('GITHUB_SECRET')
    if request.method == 'POST':
        logger.info('Webhook received')

        # Verify the signature
        signature = request.headers.get('X-Hub-Signature')
        if not signature:
            logger.error('Missing X-Hub-Signature header')
            messages.error(request, 'Missing X-Hub-Signature header')
            return render(request, 'f5rugby/nice_try.html')
        
        sha_name, signature = signature.split('=')
        if sha_name != 'sha1':
            logger.error('Invalid signature algorithm')
            messages.error(request, 'Invalid signature algorithm')
            return render(request, 'f5rugby/nice_try.html')
        
        mac = hmac.new(GITHUB_SECRET.encode('utf-8'), msg=request.body, digestmod=hashlib.sha1)
        if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
            logger.error('Invalid signature')
            messages.error(request, 'Invalid signature')
            return render(request, 'f5rugby/nice_try.html')
        
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
        messages.error(request, 'Have a nice day :)')
        return render(request, 'f5rugby/nice_try.html')
