from django.db import models
from django.urls import reverse


class Post(models.Model):
    titulo = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', max_length=220, unique=True)
    resumo = models.CharField('Resumo', max_length=255, blank=True)
    conteudo = models.TextField('Conteúdo')
    publicado = models.BooleanField('Publicado', default=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
