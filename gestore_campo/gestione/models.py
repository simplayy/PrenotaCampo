from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Campo(models.Model):
    indirizzo = models.CharField(max_length=200)
    prezzo = models.FloatField(max_length=50)
    mq = models.IntegerField(default=90)
    giocatori = models.IntegerField(default=11)
    
class Giorno(models.Model):
    giorno = models.PositiveSmallIntegerField(
        choices=(
            (1, "Lunedi"),
            (2, "Martedi"),
            (3, "Mercoledi"),
            (4, "Giovedi"),
            (5, "Venerdi"),
            (6, "Sabato"),
            (7, "Domenica")
        )
    )
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE, default=None, blank=True, null=True)


class Ora(models.Model):
    ora = models.PositiveSmallIntegerField(validators=[
            MaxValueValidator(24),
            MinValueValidator(1)
        ])
    giorni = models.ForeignKey(Giorno, on_delete=models.CASCADE, default=None, blank=True, null=True)


    



    






