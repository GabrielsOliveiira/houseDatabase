from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, Http404

from .models import Chain, Moto, Oleo, Washed
from .forms import OleoForm, ChainForm, WashedForm

# Create your views here.

def index(request):

    bike = Moto.objects.first()
    
    oil = bike.oleos.order_by("-date").first()
    washed = bike.lavagens.order_by("-date").first()
    chain = bike.correntes.order_by("-date").first()

    ultimo_oleo_corrente = bike.ultimo_oleo_corrente
    chain_oil = (ultimo_oleo_corrente.expired() if ultimo_oleo_corrente else None)

    context = {
    "itens": {"oil": oil, "washed": washed, "chain": chain, "chain_oil": chain_oil}
    }
    
    return render(request, "moto/index.html", context)

def addInfo(request:HttpRequest):

    if request.method == "POST":
        type_form = request.POST.get("form")

        forms = {"oil": OleoForm, "chain": ChainForm, "washed": WashedForm}
        form_class = forms.get(type_form)

        if form_class:
            form = form_class(request.POST)

            if form.is_valid():
                form.save()

    context = {"formOil": OleoForm(), "formWashed": WashedForm(), "formChain": ChainForm()}
    return render(request, "moto/addItem.html", context)

def history(request, type):
    bike = Moto.objects.first()
    data = None

    data = {
        "oil": bike.oleos,
        "chain": bike.correntes,
        "washed": bike.lavagens
    }.get(type)

    if data is None:
        raise Http404("Historico não encontrado!")

    form = {
        "oil": OleoForm,
        "chain": ChainForm,
        "washed": WashedForm
    }.get(type)

    allowed_orders = {
        "date_desc": "-date",
        "date_asc": "date",
        "price_desc": "-price",
        "price_asc": "price"
    }

    orders = {
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
    }.get(type)

    selected_order = request.GET.get("order", "date_desc")

    if selected_order not in allowed_orders:
        selected_order = "date_desc"

    order = allowed_orders[selected_order]
    
    data = data.order_by(order)

    context = {"data": data, "orders": orders, "form": form, "type": type}

    return render(request, "moto/history.html", context)


def delete(request, type, id):

    configs = {
        "oil": Oleo,
        "washed": Washed,
        "chain": Chain,
    }

    model = configs[type]

    obj = get_object_or_404(model, id=id)

    if request.method == "POST":
        obj.delete()

    return redirect("moto:history", type=type)

def update(request, type, id):

    configs = {
        "oil": (Oleo, OleoForm),
        "washed": (Washed, WashedForm),
        "chain": (Chain, ChainForm),
    }

    model, form_class = configs[type]

    obj = get_object_or_404(model, id=id)

    if request.method == "POST":
        form = form_class(request.POST, instance=obj)

        if form.is_valid():
            form.save()

    return redirect("moto:history", type=type)