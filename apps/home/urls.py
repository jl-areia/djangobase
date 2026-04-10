from django.urls import path
from .views import home, about, cadastro, perfil, editar_perfil

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', about, name='sobre'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
]
