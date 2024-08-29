from django.shortcuts import render
from django.http import HttpResponse
from .models import Article  # جدول رو از دیتابیس فراخونی
# میکنم تا به اطلاعاتش دسترسی داشته باشم


# Create your views here.

def home(request):
    art = Article.objects.all()
    return HttpResponse(art)
    # return HttpResponse("Hello World")