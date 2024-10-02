from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, Http404
from . import forms
from .forms import CreateArticleForm, EditArticleForm
from .models import Article, Person  # جدول رو از دیتابیس فراخونی
# میکنم تا به اطلاعاتش دسترسی داشته باشم
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    logout(request)
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

    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page') # شماره صفحه ای رو که کاربر درخواست کرده رو دریافت میکنه
    page_obj = paginator.get_page(page_number) # اطلاعات صفحه ی در خواست شده رو دریافت میکنه

    context = {
        'page_obj':page_obj
    }
    return render(request, 'Home/art_list.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'Home/detail.html', {'article':article})

@login_required(login_url='/account/log_in/')
def create_article(request):
    # if request.user.is_authenticated:  ایف و الس بررسی میکنن که ایا کاربر لاگین کرده یا نه و بجای این کار میشه از دیکوریتور استفاده کرد هر چند که اصلا بدون لاگین کردن امکان ورود وجود نداره
    print(f"Request method is : {request.method}")
    if request.method == "POST":
        form = CreateArticleForm(data=request.POST, files=request.FILES)
        print(f'request Files : {request.FILES}')
        print(f"Form is valid : {form.is_valid()}")
        if form.is_valid():
            print(form.cleaned_data)
            title = form.cleaned_data.get('Title')
            text = form.cleaned_data.get('Text')
            image = form.cleaned_data.get('Image')
            is_show = form.cleaned_data.get('is_show')
            Article.objects.create(title=title, text=text, image=image, is_show=is_show,
                                   auther=request.user)
            print("Article created")
            return redirect('home:art_list')
    else:
        form = CreateArticleForm()
    return render(request, 'Home/create_article.html', {"form":form})

@login_required(login_url='/account/log_in/')
def edit_article(request, article_id):
    art = get_object_or_404(Article, id=article_id, auther_id=request.user.id)
    print(f"Editing article: {art}")
    if request.method == "POST":
        print(f"Request method is POST")
        form = EditArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print(f"Form is valid: {form.cleaned_data}")
            art.title = form.cleaned_data.get('Title')
            art.text = form.cleaned_data.get('Text')
            image = form.cleaned_data.get('Image')
            # فقط اگر تصویر جدید بارگذاری شود، آن را به روز می‌کنیم
            if image:
                art.image = image
            art.is_show = form.cleaned_data.get('is_show')
            art.save()
            print("Article edited")
            return redirect('home:detail', article_id=article_id)
    else:
        print(f"Request method is GET")
        form = EditArticleForm(initial={
            'Title': art.title,
            'Text': art.text,
            'Image': art.image,
            'is_show': art.is_show
        })

    return render(request, 'Home/article_edit.html', {"form": form, "article": art})

def delete_article(request, article_id):
    art = get_object_or_404(Article, id=article_id, auther_id=request.user.id)
    art.delete()
    return redirect('home:art_list')


