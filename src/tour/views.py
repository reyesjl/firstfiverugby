from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'tour/index.html', context)