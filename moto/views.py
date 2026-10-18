from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ChainForm, OleoForm, WashedForm
from .models import Chain, Moto, Oleo, Washed
from .services import (
    adicionarInformacao,
    escolherFormulario,
    escolherOrdem,
    ordensPermitidas,
)


@login_required
def index(request, id):

    moto = get_object_or_404(Moto, id=id, usuario=request.user)

    oil = moto.oleos.order_by("-date").first()
    washed = moto.lavagens.order_by("-date").first()
    chain = moto.correntes.order_by("-date").first()

    ultimo_oleo_corrente = moto.ultimo_oleo_corrente
    chain_oil = ultimo_oleo_corrente.expired() if ultimo_oleo_corrente else None

    context = {
        "itens": {"oil": oil, "washed": washed, "chain": chain, "chain_oil": chain_oil},
        "moto_id": id,
    }

    return render(request, "moto/index.html", context)


@login_required
def addInfo(request: HttpRequest, id):

    if request.method == "POST":
        adicionarInformacao(request, id)

    context = {
        "formOil": OleoForm(),
        "formWashed": WashedForm(),
        "formChain": ChainForm(),
        "moto_id": id,
    }
    return render(request, "moto/addItem.html", context)


@login_required
def history(request, type, id):
    moto = Moto.objects.get(id=id, usuario=request.user)
    data = None

    data = {"oil": moto.oleos, "chain": moto.correntes, "washed": moto.lavagens}.get(
        type
    )

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

    context = {
        "data": data,
        "orders": orders,
        "form": form,
        "type": type,
        "moto_id": id,
    }

    return render(request, "moto/history.html", context)


@login_required
def delete(request, type, id):

    configs = {
        "oil": Oleo,
        "washed": Washed,
        "chain": Chain,
    }

    model = configs[type]

    obj = get_object_or_404(model, id=id, moto__usuario=request.user)

    if request.method == "POST":
        obj.delete()

    return redirect("moto:history", type=type, id=obj.moto_id)


@login_required
def update(request, type, id):

    configs = {
        "oil": (Oleo, OleoForm),
        "washed": (Washed, WashedForm),
        "chain": (Chain, ChainForm),
    }

    model, form_class = configs[type]

    obj = get_object_or_404(model, id=id, moto__usuario=request.user)

    if request.method == "POST":
        form = form_class(request.POST, instance=obj)

        if form.is_valid():
            form.save()

    return redirect("moto:history", type=type, id=obj.moto_id)


@login_required
def check_oil(request, id):
    try:
        current_kms = int(request.GET["current_kms"])
    except (KeyError, TypeError, ValueError):
        return JsonResponse({"error": "Informe uma quilometragem válida."}, status=400)

    moto = get_object_or_404(Moto, id=id, usuario=request.user)

    oil = moto.ultimo_oleo

    if oil is None:
        return JsonResponse({"error": "Nenhuma troca de óleo cadastrada."}, status=404)

    if current_kms < oil.kms:
        return JsonResponse(
            {"error": "A quilometragem não pode ser menor que a da última troca."},
            status=400,
        )

    precisa_trocar = oil.need_to_change(current_kms)

    kms_restantes = max(0, oil.kms + 1500 - current_kms)

    return JsonResponse(
        {"precisa_trocar": precisa_trocar, "kms_restantes": kms_restantes}
    )
