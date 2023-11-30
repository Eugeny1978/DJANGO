from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), # http://127.0.0.1:8000/ # домашняя страница
    path('cats/', views.categories), # http://127.0.0.1:8000/cat/
]