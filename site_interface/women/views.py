from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): #HttpRequest
    return HttpResponse('Страница Приложения women.')

def categories(request): #HttpRequest
    return HttpResponse('<h1>Статьи по Категориям</h1>')


