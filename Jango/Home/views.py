from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article  # جدول رو از دیتابیس فراخونی
# میکنم تا به اطلاعاتش دسترسی داشته باشم


# Create your views here.

def home(request):
    articles = Article.objects.all().filter(is_show=True)
    context = {
        'art':articles
    }
    return render(request, 'Home/home.html', context)

def art_list(request):
    articles = Article.objects.all().filter(is_show=True)
    context = {
        'article':articles
    }
    return render(request, 'Home/art_list.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'Home/detail.html', {'article':article})

