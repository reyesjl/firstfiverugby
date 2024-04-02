# camps/views.py
from django.shortcuts import render
from .models import Camp

def index(request):
    all_camps = Camp.objects.order_by('start_date')
    context = {'camps': all_camps}
    return render(request, 'camps/camps.html', context)