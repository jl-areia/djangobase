from django.shortcuts import render, get_object_or_404
from .models import Post


def blog(request):
    posts = Post.objects.filter(publicado=True).order_by('-criado_em')
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, publicado=True)
    return render(request, 'blog/detail.html', {'post': post})
