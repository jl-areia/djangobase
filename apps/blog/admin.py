from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'publicado', 'criado_em')
    list_filter = ('publicado', 'criado_em')
    search_fields = ('titulo', 'resumo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}
