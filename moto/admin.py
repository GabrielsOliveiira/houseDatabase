from django.contrib import admin

# Register your models here.
from .models import Chain, Moto, Oleo, Washed

admin.site.register(Washed)
admin.site.register(Oleo)
admin.site.register(Chain)
admin.site.register(Moto)