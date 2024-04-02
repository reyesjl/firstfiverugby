# f5rugby/views.py
# author: jose
# date: April 1st, 2024

from django.shortcuts import render

def index(request):
    return render(request, 'f5rugby/index.html', context={})

def camps(request):
    return render(request, 'f5rugby/camps.html', context={})

def health(request):
    return render(request, 'f5rugby/health.html', context={})
