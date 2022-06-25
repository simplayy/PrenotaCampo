from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

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

    def get_form_kwargs(self):
        kwargs = super(CreateCampoView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self, **kwargs):
        return reverse_lazy("gestione:detailcampo", kwargs={'pk': self.object.pk})

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
    def get_form_kwargs(self):
        kwargs = super( CreatePrenotazioneView, self).get_form_kwargs()
        kwargs['datap'] = self.kwargs['datap']
        kwargs['giornop'] = self.kwargs['giornop']
        kwargs['pk_campop'] = self.kwargs['pk_campop']
        kwargs['user'] = self.request.user
        return kwargs
    def get_success_url(self, **kwargs):
        return reverse_lazy("gestione:esitoprenotazione", kwargs={'pk': self.object.pk})


class CampiSituationView(GroupRequiredMixin, ListView):
    group_required = ["Dirigente"]
    model = Campo
    template_name = "gestione/lista_campi.html"

    def get_queryset(self):
        return Campo.objects.filter(utente_id=self.request.user)

    
class PrenotazioniDirigenteView(ListView):
    context_object_name = 'prenotazione'
    model = Prenotazione
    template_name = "gestione/situation.html"

    def get_queryset(self):
        return Prenotazione.objects.filter(ora__giorno__campo__utente=self.request.user)
            
    def get_context_data(self, **kwargs):
        context = super(PrenotazioniDirigenteView, self).get_context_data(**kwargs)
        return context

class PrenotazioniView(ListView):
    context_object_name = 'prenotazione'
    model = Prenotazione
    template_name = "gestione/situation.html"

    def get_queryset(self):
            return Prenotazione.objects.filter(utente_id=self.request.user)
            
    def get_context_data(self, **kwargs):
        context = super(PrenotazioniView, self).get_context_data(**kwargs)
        context['oggi'] = date.today()
        return context

class EsitoPrenotazioneView(LoginRequiredMixin, DetailView):
    model = Prenotazione
    template_name = "gestione/esito_prenotazione.html"
    sconto = "NO"
    
        
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        p = ctx["object"]
        print(p.utente_id)
        p=len(Prenotazione.objects.filter(utente_id=p.utente_id))
        print(p)
        if(p%3 == 0): 
            self.sconto="SI" 
        return ctx

class EliminaPrenotazioneView(LoginRequiredMixin, DetailView):
    model = Prenotazione
    template_name = "gestione/cancellazione.html"
    errore = "NO_ERRORS"
    
        
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        p = ctx["object"]
        print(p.utente_id)
        if p != None:

            if p.data == date.today():
                self.errore = "RETARD"

            if p.utente_id != self.request.user.pk:
                self.errore = "Prenotazione non tua!"

        else:
            self.errore = "Non esiste una prenotazione"

        if self.errore == "NO_ERRORS" or  self.errore == "RETARD":
            try:
                Prenotazione.objects.filter(id=p.id).delete()
                pass

            except Exception as e:
                print("Errore! " + str(e))
                self.errore = "Errore nell'operazione di restituzione"

        print(self.errore)
        return ctx

class EliminaGiornoView(GroupRequiredMixin, DetailView):
    group_required = ["Dirigente"]
    model = Giorno
    template_name = "gestione/cancellazione_giorno.html"
    errore = "NO_ERRORS"
    
        
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        g = ctx["object"]
        if g == None:
            self.errore = "Non esiste Il giorno selezioanto"

        if self.errore == "NO_ERRORS":
            try:
                Giorno.objects.filter(id=g.id).delete()
                pass

            except Exception as e:
                print("Errore! " + str(e))
                self.errore = "Errore nell'operazione di cancellazioen giorno"

        print(self.errore)
        return ctx

class EliminaCampoView(GroupRequiredMixin, DetailView):
    group_required = ["Dirigente"]
    model = Campo
    template_name = "gestione/cancellazione_campo.html"
    errore = "NO_ERRORS"
    
        
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        c = ctx["object"]
        if c == None:
            self.errore = "Non esiste Il campo selezioanto"

        if self.errore == "NO_ERRORS":
            try:
                Campo.objects.filter(id=c.id).delete()
                pass

            except Exception as e:
                print("Errore! " + str(e))
                self.errore = "Errore nell'operazione di cancellazioen giorno"

        print(self.errore)
        return ctx

def search(request):

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            sstring = form.cleaned_data.get("caratteristiche")
            cap = form.cleaned_data.get("cap")
            if(cap == ""): cap = "None"
            return redirect("gestione:ricerca_risultati", sstring, cap)
    else:
        form = SearchForm()

    return render(request,template_name="gestione/ricerca.html",context={"form":form})

class CampoRicercaView(CampoListView):
    titolo = "La tua ricerca ha dato come risultato"

    def get_queryset(self):
        sstring = self.request.resolver_match.kwargs["sstring"] 
        cap = self.request.resolver_match.kwargs["cap"]

        
      
        qq = self.model.objects.filter(indirizzo__icontains=sstring) | self.model.objects.filter(giocatori__icontains=sstring)
        if (cap != "None"): qq = sorted(qq, key=lambda campi: campi.confronta_distanza(cap) )



        return qq
