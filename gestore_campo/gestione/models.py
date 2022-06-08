from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Campo(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    indirizzo = models.CharField(max_length=200)
    prezzo = models.FloatField(max_length=50)
    mq = models.IntegerField(default=90)
    giocatori = models.IntegerField(default=11)
    


class Prenotazione(models.Model):
    data_prenotazione = models.DateField(default=None,null=True,blank=True)
    ora_inizio = models.IntegerField(max_length=50)
    ora_fine = models.IntegerField(max_length=50)
    campo = models.ForeignKey(Campo,on_delete=models.CASCADE,related_name="prenotazioni")
    utente = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="campi_prenotati")

    def chi_prenotato(self):
        if self.utente == None: return None
        return self.utente.username

    
    def __str__(self):
        return "Campo in via " + self.campo.indirizzo + " con id " + self.campo.id + " prenotato il " + str(self.data_prenotazione) + " per le  " + str(self.ora_inizio) + " fino alle  " + str(self.ora_fine) 

