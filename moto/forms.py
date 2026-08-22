from django import forms
from .models import Moto, Oleo, Washed, Chain

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['dono']
    dono = forms.CharField(label='Dono', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class OleoForm(forms.ModelForm):
    class Meta:
        model = Oleo
        fields = ['price', 'date', 'kms', 'moto']
    price = forms.DecimalField(label='Preço', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label='Data', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    kms = forms.IntegerField(label='Quilometragem', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    moto = forms.ModelChoiceField(label='Moto', queryset=Moto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

class WashedForm(forms.ModelForm):
    class Meta:
        model = Washed
        fields = ['date', 'moto']
    date = forms.DateField(label='Data', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    moto = forms.ModelChoiceField(label='Moto', queryset=Moto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

class ChainForm(forms.ModelForm):
    class Meta:
        model = Chain
        fields = ['date', 'moto']
    date = forms.DateField(label='Data', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    moto = forms.ModelChoiceField(label='Moto', queryset=Moto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))