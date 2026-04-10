from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo_url = models.URLField('URL da foto', blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
