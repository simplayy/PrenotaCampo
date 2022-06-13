from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

# pipenv install django-braces
from braces.views import GroupRequiredMixin


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
    success_url = reverse_lazy("gestione:aggiungigiorno")

    def get_form_kwargs(self):
        kwargs = super(CreateCampoView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class CreateGiornoView(CreateView):
    title = "Aggiungi un giorno"
    form_class = CreateGiornoForm
    template_name = "gestione/create_entry.html"
    success_url = reverse_lazy("gestione:home")
    def get_form_kwargs(self):
        kwargs = super(CreateGiornoView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['pk_campo'] = self.kwargs['pk_campo']
        return kwargs

class CreateOraView(CreateView):
    title = "Aggiungi un ora "
    form_class = CreateOraForm
    template_name = "gestione/create_entry.html"
    success_url = reverse_lazy("gestione:aggiungiora")

    def get_form_kwargs(self):
        kwargs = super(CreateOraView, self).get_form_kwargs()
        kwargs['pk_campo'] = self.kwargs['pk_campo']
        kwargs['pk_giorno'] = self.kwargs['pk_giorno']
        return kwargs


class CampoDetailView(DetailView):
    titolo = "Dettagli campo"
    context_object_name = 'campo'
    model = Campo
    template_name = "gestione/detailcampo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['giorno'] = Giorno.objects.filter(campo_id=self.kwargs['pk'])
        return context

class CampiSituationView(GroupRequiredMixin, ListView):
    group_required = ["Dirigente"]
    model = Campo
    template_name = "gestione/situationc.html"

    def get_queryset(self):
        return Campo.objects.filter(utente_id=self.request.user)


    