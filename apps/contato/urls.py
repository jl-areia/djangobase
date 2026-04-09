from django.urls import path
from .views import contato

urlpatterns = [
    path('', contato, name='contato'),
]
