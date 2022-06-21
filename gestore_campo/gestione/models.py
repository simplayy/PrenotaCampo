from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Campo(models.Model):
    indirizzo = models.CharField(max_length=200)
    prezzo = models.FloatField(max_length=50)
    mq = models.IntegerField(default=90)
    giocatori = models.IntegerField(default=11)
    utente = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="campi_posseduti")

    def __str__(self):
        return  self.indirizzo + " a "+ str(self.giocatori)
    
class Giorno(models.Model):
    giorno = models.SmallIntegerField(
        choices=(
            (0, "Lunedi"),
            (1, "Martedi"),
            (2, "Mercoledi"),
            (3, "Giovedi"),
            (4, "Venerdi"),
            (5, "Sabato"),
            (6, "Domenica")
        ) 
    )
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE, default=None, blank=True, null=True)

    class Meta:
        unique_together = ('giorno', 'campo')


    def __str__(self):
        giorni ={

            0: "Lunedi",
            1: "Martedi",
            2: "Mercoledi",
            3: "Giovedi",
            4: "Venerdi",
            6: "Domenica"

            }
        return giorni.get(self.giorno, "invalido")



class Ora(models.Model):
    ora = models.PositiveSmallIntegerField(validators=[
            MaxValueValidator(24),
            MinValueValidator(1)
        ])
    giorno = models.ForeignKey(Giorno, on_delete=models.CASCADE, default=None, blank=True, null=True)
    class Meta:
        unique_together = ('giorno', 'ora')
        
    def __str__(self):
        return str(self.ora) +":00 - " + str(self.ora + 1)  + ":00 "

class Prenotazione(models.Model):
    data = models.DateField()
    ora = models.ForeignKey(Ora, on_delete=models.CASCADE, default=None, blank=True, null=True)
    utente = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="utente")
    class Meta:
        unique_together = ('data', 'ora')




