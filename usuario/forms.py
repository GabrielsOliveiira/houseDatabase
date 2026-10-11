from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email']
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail', 'class': 'form-control'}))