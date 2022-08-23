from django.contrib import admin
# добавить модель (таблицу) 
from .models import Project

# регистрируем ее чтобы она появилась в админке
admin.site.register(Project)
