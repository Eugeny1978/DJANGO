from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify # фильтры

# Create your views here.

# menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить Статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

AJ_content = '''<h3>Анджелина Джоли</h3> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) 
    — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».'''

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': AJ_content, 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]


def index(request): #HttpRequest
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'главная страница',
        'menu': menu,
        # 'main_title': 'главная страница',
        # 'float': 27.789,
        # 'lst': [1, 4, 'asv', True],
        # 'set': {1, 2, 5, 4, 2, 7},
        # 'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        # 'obj': MyClass(10, 20),
        # 'url': slugify('slugify The main page')
        'posts': data_db
    }
    return render(request, 'women/index.html', context=data)

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def about(request):
    data = {
        'title': 'о сайте',
        'menu': menu
    }
    return render(request, 'women/about.html', context=data) #

def add_page(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена.</h1>')


# def categories(request, cat_id): #HttpRequest
#     return HttpResponse(f'<h1>Статьи по Категориям</h1><p>id: {cat_id}</p>')
#
# def categories_by_slug(request, cat_slug):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f'<h1>Статьи по Категориям</h1><p>slug: {cat_slug}</p>')
#
# def archive(request, year):
#     if year > 2023:
#         # raise Http404()
#         # return redirect('/') # Начальный Адрес или конкретный адрес
#         # return redirect(index) # Через Функцию представления
#         # return redirect('/', permanent=True) # 301 - постоянная ссылка перенаправления если Ложь - 302 временная
#         # return redirect('home') # Через Имя Функиции представления - рекомендуемый способ перенаправления
#         # return redirect('cats', 'music')
#         uri = reverse('cats', args=('music', ))
#         # return redirect(uri)
#         # return HttpResponseRedirect(uri)
#         return HttpResponsePermanentRedirect()
#     return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')

