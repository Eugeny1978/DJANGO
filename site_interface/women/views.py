from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): #HttpRequest
    return HttpResponse('Страница Приложения women.') #!

def categories(request, cat_id): #HttpRequest
    return HttpResponse(f'<h1>Статьи по Категориям</h1><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по Категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')