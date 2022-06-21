from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
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
    success_url = reverse_lazy("gestione/?operation=ok")

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

        


class SelezionaDataFormView(FormView):
    template_name = 'gestione/create_entry.html'
    form_class = SelezionaDataForm
    
    
    def get_success_url(self):
        return reverse_lazy('gestione:aggiungiprenotazione', kwargs={'giornop': self.giorno, 'datap': self.date, 'pk_campop': self.kwargs['pk_campo']  })

    def form_valid(self, form):
        self.giorno=form.cleaned_data["date"].weekday()
        self.date=form.cleaned_data["date"]
        return super().form_valid(form)

class CreatePrenotazioneView(CreateView):
    title = "Aggiungi Prenotazione"
    form_class =  CreatePrenotazioneForm
    template_name = "gestione/create_entry.html"
    success_url = reverse_lazy("gestione:home")
    def get_form_kwargs(self):
        kwargs = super( CreatePrenotazioneView, self).get_form_kwargs()
        kwargs['datap'] = self.kwargs['datap']
        kwargs['giornop'] = self.kwargs['giornop']
        kwargs['pk_campop'] = self.kwargs['pk_campop']
        
        return kwargs

class CreatePreView(CreateView):
    title = "Aggiungi un sdora "
    form_class = CreatedioForm
    template_name = "gestione/create_entry.html"
    success_url = reverse_lazy("gestione/?operation=ok")
    
    def get_form_kwargs(self):
        kwargs = super(CreatePreView, self).get_form_kwargs()
        kwargs['datat'] = self.kwargs['datat']
        kwargs['giornot'] = self.kwargs['giornot']
        kwargs['pk_campot'] = self.kwargs['pk_campot']
        return kwargs

class CampiSituationView(GroupRequiredMixin, ListView):
    group_required = ["Dirigente"]
    model = Campo
    template_name = "gestione/lista_campi.html"

    def get_queryset(self):
        return Campo.objects.filter(utente_id=self.request.user)


class PrenotazioniView(ListView):
    context_object_name = 'prenotazione'
    model = Prenotazione
    template_name = "gestione/situation.html"

class EliminaPrenotazioneView(LoginRequiredMixin, DetailView):
    model = Prenotazione
    template_name = "gestione/cancellazione.html"
    errore = "NO_ERRORS"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        p = ctx["object"]
        print(p)
        # if c.data_prestito != None:

        #     if c.utente.pk != self.request.user.pk:
        #         self.errore = "Non puoi restituire un libro non tuo!"

        # else:
        #     self.errore = "Libro attualmente non in prestito"

        # if self.errore == "NO_ERRORS":
        #     try:
        #         c.data_prestito = None
        #         c.utente = None
        #         c.save()
        #     except Exception as e:
        #         print("Errore! " + str(e))
        #         self.errore = "Errore nell'operazione di restituzione"

        return ctx