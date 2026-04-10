from django.urls import path
from .views import blog, criar_post, post_detail, editar_post

urlpatterns = [
    path('', blog, name='blog'),
    path('criar/', criar_post, name='criar_post'),
    path('editar/<int:pk>/', editar_post, name='editar_post'),
    path('<int:pk>/', post_detail, name='post_detail'),
]
