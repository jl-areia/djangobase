from django.urls import path
from .views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', about, name='sobre'),
]
