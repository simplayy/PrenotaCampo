from django.db import models

# Create your models here.
class Campo(models.Model):
    indirizzo = models.CharField(max_length=200)
    prezzo = models.FloatField(max_length=50)
    mq = models.IntegerField(default=100)
