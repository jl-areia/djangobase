from django.shortcuts import render
from apps.blog.models import Post


def home(request):
    recentes = Post.objects.filter(publicado=True).order_by('-criado_em')[:3]
    return render(request, 'home/index.html', {'posts': recentes})


def about(request):
    return render(request, 'home/about.html')
