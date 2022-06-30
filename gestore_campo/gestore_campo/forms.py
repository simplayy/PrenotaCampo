from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

# form per la creazioen di un utente clienti
class CreaUtenteCliente(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit) 
        g = Group.objects.get(name="Clienti")
        g.user_set.add(user) 
        return user 

# form per la creazioen di un utente dirigente
class CreaUtenteDirigente(UserCreationForm):
    
    def save(self, commit=True):
        user = super().save(commit) 
        g = Group.objects.get(name="Dirigenti") 
        g.user_set.add(user) 
        return user 
