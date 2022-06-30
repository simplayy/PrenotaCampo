from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin


# view per la creazione di un cliente
class UserCreateView(CreateView):
    form_class = CreaUtenteCliente
    template_name = "user_create.html"
    success_url = reverse_lazy("login")

# view per la creazione di un dirigente
class DirigenteCreateView(PermissionRequiredMixin, UserCreateView):
    permission_required = "is_staff"
    form_class = CreaUtenteDirigente