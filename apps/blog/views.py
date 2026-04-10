from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Comment, Post, Categoria, Reaction, Tag


def blog(request):
    posts = Post.objects.all().order_by('-criado_em')
    return render(request, 'blog/index.html', {'posts': posts})


def criar_post(request):
    categorias = Categoria.objects.all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        post = Post.objects.create(
            titulo=request.POST['titulo'],
            conteudo=request.POST['conteudo'],
            categoria_id=request.POST.get('categoria') or None,
            autor=request.user if request.user.is_authenticated else None,
            video_url=request.POST.get('video_url', '').strip() or '',
            gif_url=request.POST.get('gif_url', '').strip() or ''
        )

        tags_ids = request.POST.getlist('tags')
        post.tags.set(tags_ids)

        return redirect('blog')

    return render(request, 'blog/criar.html', {
        'categorias': categorias,
        'tags': tags
    })


@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.autor != request.user and not request.user.is_superuser:
        raise Http404

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/editar.html', {
        'form': form,
        'post': post,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST' and 'emoji' in request.POST and request.user.is_authenticated:
        emoji = request.POST.get('emoji')
        valid_emojis = ['🤩', '🚀', '😂', '👌', '🤖', '👍', '👎']
        if emoji in valid_emojis:
            Reaction.objects.get_or_create(post=post, user=request.user, emoji=emoji)
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST' and 'mensagem' in request.POST:
        nome = request.POST.get('nome', request.user.username if request.user.is_authenticated else 'Visitante').strip() or 'Visitante'
        mensagem = request.POST.get('mensagem', '').strip()
        if mensagem:
            Comment.objects.create(
                post=post,
                user=request.user if request.user.is_authenticated else None,
                nome=nome,
                mensagem=mensagem
            )
            return redirect('post_detail', pk=post.pk)

    if request.method == 'GET':
        post.visualizacoes = post.visualizacoes + 1
        post.save(update_fields=['visualizacoes'])

    reaction_counts = list(post.reactions.values('emoji').annotate(count=Count('id')).order_by('-count'))
    if request.user.is_authenticated:
        user_reactions = list(post.reactions.filter(user=request.user).values_list('emoji', flat=True))
    else:
        user_reactions = []

    comments = post.comments.all()
    suggested_comments = [
        {
            'nome': 'Leitor Visionário',
            'mensagem': 'Esse post ficou com um visual impressionante! Os vídeos deixam o conteúdo mais vivo.'
        },
        {
            'nome': 'Fã do Futuro',
            'mensagem': 'Curti muito a combinação de GIFs e texto. Parece mesmo uma rede social moderna.'
        },
        {
            'nome': 'Comentador Ativo',
            'mensagem': 'Queria ver mais posts assim, com interação e mídia integrada.'
        }
    ]
    admin_profile = {
        'nome': 'Julimar Lemos',
        'cargo': 'Administrador do blog',
        'bio': 'Criação de conteúdo, curadoria e cuidado com a experiência visual do site.'
    }
    reaction_emojis = ['🤩', '🚀', '😂', '👌', '🤖', '👍', '👎']
    return render(request, 'blog/detail.html', {
        'post': post,
        'comments': comments,
        'suggested_comments': suggested_comments,
        'admin_profile': admin_profile,
        'reaction_counts': reaction_counts,
        'user_reactions': user_reactions,
        'reaction_emojis': reaction_emojis,
    })
