from django import forms
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Seu nome completo',
                'class': 'input-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@dominio.com',
                'class': 'input-control',
            }),
            'mensagem': forms.Textarea(attrs={
                'placeholder': 'Escreva sua mensagem...',
                'rows': 5,
                'class': 'input-control',
            }),
        }
