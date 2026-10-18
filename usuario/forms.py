from django import forms

from .models import Usuario


class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Digite sua senha", "class": "form-control"}
        ),
    )

    first_name = forms.CharField(
        label="Nome",
        max_length=150,
        widget=forms.TextInput(
            attrs={"placeholder": "Digite seu nome", "class": "form-control"}
        ),
    )

    class Meta:
        model = Usuario
        fields = ["first_name", "email"]

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Digite seu e-mail", "class": "form-control"}
        )
    )
