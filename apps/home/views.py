from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count, Sum
from django.shortcuts import render, redirect

from apps.blog.models import Comment, Post, Reaction
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Profile


def home(request):
    recentes = Post.objects.all().order_by('-criado_em')[:3]
    return render(request, 'home/index.html', {'posts': recentes})


def about(request):
    return render(request, 'home/about.html')


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def perfil(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    posts_criados = Post.objects.filter(autor=request.user).count()
    posts_comentados = Comment.objects.filter(user=request.user).count()
    posts_reagidos = Reaction.objects.filter(user=request.user).count()
    visitas_totais = Post.objects.filter(autor=request.user).aggregate(total=Sum('visualizacoes'))['total'] or 0

    return render(request, 'profile.html', {
        'usuario': request.user,
        'profile': profile,
        'posts_criados': posts_criados,
        'posts_comentados': posts_comentados,
        'posts_reagidos': posts_reagidos,
        'visitas_totais': visitas_totais,
    })


@login_required
def editar_perfil(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso.')
            return redirect('perfil')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
