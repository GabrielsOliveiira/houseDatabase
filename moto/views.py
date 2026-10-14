from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, Http404

from .models import Chain, Moto, Oleo, Washed
from .forms import OleoForm, ChainForm, WashedForm

from .services import adicionarInformacao, escolherFormulario, escolherOrdem, ordensPermitidas

# Create your views here.

def index(request, id):

    moto = get_object_or_404(Moto, id=id)
    
    oil = moto.oleos.order_by("-date").first()
    washed = moto.lavagens.order_by("-date").first()
    chain = moto.correntes.order_by("-date").first()

    ultimo_oleo_corrente = moto.ultimo_oleo_corrente
    chain_oil = (ultimo_oleo_corrente.expired() if ultimo_oleo_corrente else None)

    context = {
    "itens": {"oil": oil, "washed": washed, "chain": chain, "chain_oil": chain_oil}, "moto_id": id
    }
    
    return render(request, "moto/index.html", context)

def addInfo(request:HttpRequest, id):

    if request.method == "POST":
        adicionarInformacao(request, id)

    context = {"formOil": OleoForm(), "formWashed": WashedForm(), "formChain": ChainForm(), "moto_id": id}
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

    form = escolherFormulario(type)

    allowed_orders = ordensPermitidas()

    orders = escolherOrdem(type)

    selected_order = request.GET.get("order", "date_desc")

    if selected_order not in allowed_orders:
        selected_order = "date_desc"

    order = allowed_orders[selected_order]
    
    data = data.order_by(order)

    context = {"data": data, "orders": orders, "form": form, "type": type, "moto_id": bike.id}

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