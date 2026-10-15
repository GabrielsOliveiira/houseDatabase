from django import forms
from .models import Moto, Oleo, Washed, Chain

class motoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['cor', 'placa']

    cor = forms.CharField(
        label='Cor',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite a cor da moto'
        })
    )

    placa = forms.CharField(
        label='Placa',
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite a placa da moto'
        })
    )

class OleoForm(forms.ModelForm):
    class Meta:
        model = Oleo
        fields = ['price', 'date', 'kms']
    price = forms.DecimalField(label='Preço', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label='Data', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    kms = forms.IntegerField(label='Quilometragem', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # moto = forms.ModelChoiceField(label='Moto', queryset=Moto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

class WashedForm(forms.ModelForm):
    class Meta:
        model = Washed
        fields = ['date']
    date = forms.DateField(label='Data', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    # moto = forms.ModelChoiceField(label='Moto', queryset=Moto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

class ChainForm(forms.ModelForm):
    class Meta:
        model = Chain
        fields = ['date']
    date = forms.DateField(label='Data', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    # moto = forms.ModelChoiceField(label='Moto', queryset=Moto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))