from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome', required=False)
    last_name = forms.CharField(label='Sobrenome', required=False)
    email = forms.EmailField(label='E-mail', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    photo_url = forms.URLField(label='URL da foto', required=False,
                               widget=forms.URLInput(attrs={'placeholder': 'https://...'}))

    class Meta:
        model = Profile
        fields = ['photo_url']
