from django.shortcuts import get_object_or_404

from .models import Moto
from .forms import OleoForm, ChainForm, WashedForm

def salvarInformacaoMoto(form, moto):
    item = form.save(commit=False)
    item.moto = moto
    item.save()

def escolherFormulario(escolhido):
    forms = {"oil": OleoForm, "chain": ChainForm, "washed": WashedForm}
    return forms.get(escolhido)

def escolherOrdem(escolhido):
    return {
        "oil": [
            ("date_desc", "Data mais recente"),
            ("date_asc", "Data mais antiga"),
            ("price_desc", "Maior preço"),
            ("price_asc", "Menor preço")
        ],

        "chain": [
            ("date_desc", "Data mais recente"),
            ("date_asc", "Data mais antiga")
        ],
        "washed": [
            ("date_desc", "Data mais recente"),
            ("date_asc", "Data mais antiga")
        ]
    }.get(escolhido)

def ordensPermitidas():
    return {
        "date_desc": "-date",
        "date_asc": "date",
        "price_desc": "-price",
        "price_asc": "price"
    }

def adicionarInformacao(request, id):
    moto = get_object_or_404(Moto, id=id)

    type_form = request.POST.get("form")

    form_class = escolherFormulario(type_form)

    if form_class:
        form = form_class(request.POST)

        if form.is_valid():
            salvarInformacaoMoto(form, moto)