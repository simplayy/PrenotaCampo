from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

from .utils import cap_to_lat, cap_to_lng, calc_dist_fixed, cap_to_comune


# Classe per definire il modello di un campo
class Campo(models.Model):
    indirizzo = models.CharField(max_length=200)
    prezzo = models.FloatField(max_length=50)
    mq = models.IntegerField(default=90)
    giocatori = models.IntegerField(default=11)
    utente = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="campi_posseduti")
    cap = models.IntegerField()
    immagine = models.ImageField(upload_to='campo', default="campo/default.jpg")
    tipo_erba = models.CharField(
        choices=(
            ("Sintetico", "Sintetico"),
            ("Erba Vera", "Erba Vera"),
            ("Cementato Esterno", "Cementato Esterno"),
            ("Cementato Interno", "Cementato Interno")
        ), max_length=100
    )

    def __str__(self):
        return  self.indirizzo + " a "+ str(self.giocatori)

    # metodo che calcolo la caparra di un campo pari al 20% del totale
    @property
    def caparra(self):
        return int(self.prezzo * self.giocatori * 2 * 0.20)

    # metodo che calcola il totale
    @property
    def totale(self):
        return int(self.prezzo * self.giocatori * 2 )

    # metodo che calcola il totale scontato del 15%
    @property
    def totale_scontato(self):
        return int(self.prezzo * self.giocatori * 2 * 0.85)

    # metodo che calcola la latitudine in base al cap
    @property
    def lat(self):
        return cap_to_lat(self.cap)

    # metodo che calcola la longitudine in base al cap
    @property
    def lng(self):
        return cap_to_lng(self.cap)

    # metodo che calcola il comune in base al cap
    @property
    def comune(self):
        return cap_to_comune(self.cap)

    # metodo che calcola la media di tutte le recensioni
    @property
    def rating_avg(self):
      rate = self.campo_recensito.aggregate(Avg('stelle'))
      return rate['stelle__avg']
    
    # metodo confronta la distanza di un campo da un altro cap
    def confronta_distanza(self, cap):
        return calc_dist_fixed(self.lat, self.lng, cap_to_lat(cap), cap_to_lng(cap))

    class Meta:
       ordering = ['prezzo']


# Classe per definire il modello di un giorno
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


# Classe per definire il modello di un ora
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

# Classe per definire il modello di una prenotazione
class Prenotazione(models.Model):
    data = models.DateField()
    ora = models.ForeignKey(Ora, on_delete=models.CASCADE, default=None, blank=True, null=True)
    utente = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="utente")
    class Meta:
        unique_together = ('data', 'ora')
        ordering = ['-data']

# Classe per definire il modello di una recensione
class Recensione(models.Model):
    utente = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="utente_recensore")
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="campo_recensito")
    stelle = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    descrizione = models.CharField(max_length=300)

    class Meta:
        unique_together = ('utente', 'campo')

