from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index), # http://127.0.0.1:8000/ # домашняя страница
    path('cats/<int:cat_id>/', views.categories), # http://127.0.0.1:8000/cats/1/
    path('cats/<slug:cat_slug>/', views.categories_by_slug), # http://127.0.0.1:8000/cats/latinsymbols/
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive), # http://127.0.0.1:8000/archive/2012/
]