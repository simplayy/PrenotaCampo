from django.contrib import admin
from .models import Campo, Giorno, Ora, Prenotazione
# Register your models here.
admin.site.register(Campo)
admin.site.register(Giorno)
admin.site.register(Ora)
admin.site.register(Prenotazione)