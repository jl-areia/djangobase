from django.contrib import admin
from .models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    readonly_fields = ('criado_em',)
    search_fields = ('nome', 'email', 'mensagem')
    list_filter = ('criado_em',)
