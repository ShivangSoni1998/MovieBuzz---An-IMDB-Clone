from django import forms
from .models import Movie
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'rank', 'genres', 'description', 'director', 'actor']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'rank': forms.TextInput(attrs={'class': 'form-control'}),
            'genres': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'actor': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']