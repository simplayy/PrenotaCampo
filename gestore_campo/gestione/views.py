from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.


def gestione_home(request):
    return render(request,template_name="gestione/home.html")

class CampoListView(ListView):
    titolo = "Lista Campi"
    model = Campo
    template_name = "gestione/lista_campi.html"


class CamposListView(ListView):
    titolo = "Lista Campi"
    model = Campo
    template_name = "gestione/lista_campi.html"

class CreateCampoView(CreateView):
    title = "Aggiungi un campo"
    form_class = CreateCampoForm
    template_name = "gestione/create_entry.html"
    success_url = reverse_lazy("gestione:home")


class CampoDetailView(DetailView):
    titolo = "Dettagli campo"
    model = Campo
    template_name = "gestione/detailcampo.html"