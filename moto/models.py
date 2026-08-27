from django.db import models
from datetime import date

# Create your models here.
class Moto(models.Model):
    dono = models.CharField(max_length=100)

    def __str__(self):
        return f"Dono: {self.dono}"

    @property
    def ultimo_oleo(self):
        return self.oleos.order_by("-date").first()

    @property
    def ultimo_lavado(self):
        return self.lavagens.order_by("-date").first()

    @property
    def ultimo_oleo_corrente(self):
        return self.correntes.order_by("-date").first()

class Oleo(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    kms = models.IntegerField()
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="oleos")

    def __str__(self):
        return f"Preço: {self.price} na data: {self.date} enquanto ela tinha {self.kms} kms rodados."
    
    def need_to_change(self, current_kms):
        return (current_kms-self.kms >= 1500) 

class Washed(models.Model):
    date = models.DateField()
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="lavagens")

    def __str__(self):
        return f"Data: {self.date}"

    def expired(self, data=None):

        if data is None:
            today_minus_date = (date.today()-self.date).days
            return today_minus_date >= 7

        given_date_minus_date = ((data-self.date).days)
        return given_date_minus_date > 7

class Chain(models.Model):
    date = models.DateField()
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="correntes")

    def __str__(self):
        return f"Data: {self.date}"

    def expired(self, data=None):

        if data is None:
            today_minus_date = (date.today()-self.date).days
            return today_minus_date >= 7

        given_date_minus_date = ((data-self.date).days)
        return given_date_minus_date > 7