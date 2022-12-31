from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE, null=True)
    name = models.CharField(("Profil adı"), max_length=50)
    image = models.FileField(("Profil resmi"), max_length=100)
