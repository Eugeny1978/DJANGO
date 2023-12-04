from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string



# Create your views here.

def index(request): #HttpRequest
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    return render(request, 'women/index.html')

def about(request):
    return render(request, 'women/about.html')

def categories(request, cat_id): #HttpRequest
    return HttpResponse(f'<h1>Статьи по Категориям</h1><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по Категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        # raise Http404()
        # return redirect('/') # Начальный Адрес или конкретный адрес
        # return redirect(index) # Через Функцию представления
        # return redirect('/', permanent=True) # 301 - постоянная ссылка перенаправления если Ложь - 302 временная
        # return redirect('home') # Через Имя Функиции представления - рекомендуемый способ перенаправления
        # return redirect('cats', 'music')
        uri = reverse('cats', args=('music', ))
        # return redirect(uri)
        # return HttpResponseRedirect(uri)
        return HttpResponsePermanentRedirect()
    return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена.</h1>')