from django.contrib import admin

# Register your models here.
from .models import Moto, Washed, Oleo, Chain

admin.site.register(Washed)
admin.site.register(Oleo)
admin.site.register(Chain)
admin.site.register(Moto)