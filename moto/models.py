from django.db import models

# Create your models here.
class Moto(models.Model):
    dono = models.CharField(max_length=100)

    def __str__(self):
        return f"Dono: {self.dono}"

class Oleo(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    kms = models.IntegerField()
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="oleos")

    def __str__(self):
        return f"Preço: {self.price} na data: {self.date} enquanto ela tinha {self.kms} kms rodados."

class Washed(models.Model):
    date = models.DateField()
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="lavagens")

    def __str__(self):
        return f"Data: {self.date}"

class Chain(models.Model):
    date = models.DateField()
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="correntes")

    def __str__(self):
        return f"Data: {self.date}"