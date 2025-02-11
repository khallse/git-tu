from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse ,Http404
from . import models
from django.core.paginator import Paginator

# Create your views here.

def home(request,page=0):

    articles = models.Article.objects.filter(status='P')
    paginator = Paginator(articles, 2)
    articles = paginator.get_page(page)
    context = {
        'articles' : articles ,

    }
    return render(request, 'blog/home.html', context)

def detail(request, slug):

    article = get_object_or_404(models.Article, slug=slug)

    context = {
        'article' : article,
    }
    return render(request, 'blog/detail.html', context)

def category(request, slug,page=1):

    category = get_object_or_404(models.Category,slug=slug ,status = True)
    articles = category.articles.published()
    paginator = Paginator(articles, 2)
    articles = paginator.get_page(page)
    context = {
        'articles' : articles,
        'category' :category,
    }
    return render(request, 'blog/category.html', context)