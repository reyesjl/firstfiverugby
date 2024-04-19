from django.shortcuts import render
from django.contrib import messages
from .models import Article

def index(request):
    all_articles = Article.objects.order_by('publication_date')
    context = {
        'articles': all_articles,
    }
    return render(request, 'blog/index.html', context)

def details(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        messages.error(request, "This article does not exist.")
        return render(request, 'f5rugby/error.html')
    
    context = {
        'article': article,
    }

    return render(request, 'blog/details.html', context)