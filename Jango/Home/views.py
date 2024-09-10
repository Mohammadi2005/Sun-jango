from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from . import forms
from .forms import CreateArticleForm
from .models import Article, Person  # جدول رو از دیتابیس فراخونی
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
    search_line = request.GET.get('search')
    if search_line:
        articles = articles.filter(title__icontains=search_line)
    context = {
        'article':articles
    }
    return render(request, 'Home/art_list.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'Home/detail.html', {'article':article})

def create_article(request):
    print(f"Request method is : {request.method}")
    if request.method == "GET":
        form = CreateArticleForm()
    else:
        form = CreateArticleForm(data=request.POST, files=request.FILES)
        print(f'request Files : {request.FILES}')
        print(f"Form is valid : {form.is_valid()}")
        if form.is_valid():
            print(form.cleaned_data)
            title = form.cleaned_data.get('Title')
            text = form.cleaned_data.get('Text')
            image = form.cleaned_data.get('Image')
            is_show = form.cleaned_data.get('is_show')
            author_id = form.cleaned_data.get('auther')
            person = get_object_or_404(Person, id=author_id)
            Article.objects.create(title=title, text=text, image=image, is_show=is_show, auther=person)
            print("Article created")
            return redirect('home:art_list')
    return render(request, 'Home/create_article.html', {"form":form})


