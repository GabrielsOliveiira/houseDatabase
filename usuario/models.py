from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    def __str__(self):
        return self.get_full_name() or self.email