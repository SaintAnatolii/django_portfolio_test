from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    # blogs = Blog.objects.all()
    # если нужно показать отсортированные от новых к старым и какое-то определенное кол-во
    blogs = Blog.objects.all().order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})