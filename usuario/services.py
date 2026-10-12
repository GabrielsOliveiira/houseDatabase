from moto.models import Moto
from .models import Usuario

def deleteMoto(moto_id):
    moto = Moto.objects.filter(id=moto_id)
    moto.delete()

def adicionarMoto():
    user = Usuario.objects.first()
    Moto.objects.create(usuario=user)