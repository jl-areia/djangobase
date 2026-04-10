from django.conf import settings
from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    video_url = models.URLField('URL do vídeo', max_length=500, blank=True)
    gif_url = models.URLField('URL do GIF', max_length=500, blank=True)
    visualizacoes = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    nome = models.CharField('Nome', max_length=120)
    mensagem = models.TextField('Comentário')
    criado_em = models.DateTimeField('Publicado em', auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.nome} em {self.post.titulo}'


class Reaction(models.Model):
    REACTION_CHOICES = [
        ('🤩', '🤩'),
        ('🚀', '🚀'),
        ('😂', '😂'),
        ('👌', '👌'),
        ('🤖', '🤖'),
        ('👍', '👍'),
        ('👎', '👎'),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reactions')
    emoji = models.CharField(max_length=4, choices=REACTION_CHOICES, default='👍')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user', 'emoji')
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.user.username} reagiu {self.emoji} em {self.post.titulo}'
