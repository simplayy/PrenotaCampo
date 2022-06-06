from .models import *
from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.


def gestione_home(request):
    return render(request,template_name="gestione/home.html")

class CampoListView(ListView):
    titolo = "Lista Campi"
    model = Campo
    template_name = "gestione/lista_campi.html"
