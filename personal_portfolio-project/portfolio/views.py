from django.shortcuts import render
# импортируем модель из БД
from .models import Project

def home(request):
    # передаем ее функции обработчику главной страницы
    projects = Project.objects.all()
    # передаем список результатов в шаблон
    return render(request, 'portfolio/home.html', {'projects': projects})
