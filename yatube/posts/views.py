from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Cтраницы, на которых будут посты, отфильтрованные по группам
def group_posts(request, slug):
    return HttpResponse(f'Посты группы {slug}')