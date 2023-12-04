from django.urls import path, include, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'), # http://127.0.0.1:8000/ # домашняя страница
    path('about/', views.about, name='about'), #
    path('cats/<int:cat_id>/', views.categories, name='cats_id'), # http://127.0.0.1:8000/cats/1/
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'), # http://127.0.0.1:8000/cats/latinsymbols/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive), # http://127.0.0.1:8000/archive/2012/
    path('archive/<year4:year>/', views.archive, name='archive')
]