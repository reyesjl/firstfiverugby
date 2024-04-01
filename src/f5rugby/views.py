# f5rugby/views.py
# author: jose
# date: Friday, March 29th 2024

from django.shortcuts import render

def index(request):
    return render(request, 'f5rugby/index.html', context={})
