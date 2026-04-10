from django.contrib import admin
from .models import Post, Categoria, Tag, Comment


class CustomAdminSite(admin.AdminSite):
    site_header = "Painel Futurista"
    site_title = "Admin"
    index_title = "Controle do Site"


admin_site = CustomAdminSite(name='custom_admin')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'criado_em')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('categoria', 'criado_em')
    filter_horizontal = ('tags',)

    class Media:
        css = {
            'all': ('css/admin.css',)
        }


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    class Media:
        css = {
            'all': ('css/admin.css',)
        }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    class Media:
        css = {
            'all': ('css/admin.css',)
        }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'post', 'criado_em')
    search_fields = ('nome', 'mensagem')
    list_filter = ('criado_em',)

    class Media:
        css = {
            'all': ('css/admin.css',)
        }
