from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'categoria', 'tags', 'video_url', 'gif_url']
        widgets = {
            'conteudo': forms.Textarea(attrs={
                'rows': 8,
                'placeholder': 'Escreva o conteúdo do post aqui...',
            }),
            'tags': forms.CheckboxSelectMultiple()
        }
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'categoria': 'Categoria',
            'tags': 'Tags',
            'video_url': 'URL do vídeo',
            'gif_url': 'URL do GIF',
        }
