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

# pipenv install django-braces
from braces.views import GroupRequiredMixin


# view per la lista di tutti i campi
class CampoListView(ListView):
    titolo = "Lista Campi"
    model = Campo
    template_name = "gestione/lista_campi.html"

# view per la creazione di un campo
class CreateCampoView(GroupRequiredMixin, CreateView):
    group_required = ["Dirigenti"]
    title = "Aggiungi un campo"
    form_class = CreateCampoForm
    template_name = "gestione/create_entry.html"

    def get_form_kwargs(self):
        kwargs = super(CreateCampoView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self, **kwargs):
        return reverse_lazy("gestione:detailcampo", kwargs={'pk': self.object.pk})

# view per la creazione di un giorno di disponibilita'
class CreateGiornoView(GroupRequiredMixin, CreateView):
    group_required = ["Dirigenti"]
    title = "Aggiungi un giorno"
    form_class = CreateGiornoForm
    template_name = "gestione/create_entry.html"
    success_url = reverse_lazy("gestione:home")
    def get_form_kwargs(self):
        kwargs = super(CreateGiornoView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['pk_campo'] = self.kwargs['pk_campo']
        return kwargs
    def get_success_url(self, **kwargs):
        return reverse_lazy("gestione:detailcampo", kwargs={'pk': self.kwargs['pk_campo']})

# view per la creazione di un ora di disponibilita' di un giorno
class CreateOraView(GroupRequiredMixin, CreateView):
    group_required = ["Dirigenti"]
    title = "Aggiungi un ora "
    form_class = CreateOraForm
    template_name = "gestione/create_entry.html"

    def get_form_kwargs(self):
        kwargs = super(CreateOraView, self).get_form_kwargs()
        kwargs['pk_campo'] = self.kwargs['pk_campo']
        kwargs['pk_giorno'] = self.kwargs['pk_giorno']
        return kwargs

    def get_success_url(self, **kwargs):
        return reverse_lazy("gestione:detailcampo", kwargs={'pk': self.kwargs['pk_campo']})

# view per la creazione di una recensione
class CreateRecensioneView(LoginRequiredMixin, CreateView):
    title = "Aggiungi una Recensione"
    form_class = CreateRecensioneForm
    template_name = "gestione/create_entry.html"

    def get_form_kwargs(self):
        kwargs = super(CreateRecensioneView, self).get_form_kwargs()
        kwargs['utente'] = self.request.user
        kwargs['pk_campo'] = self.kwargs['pk_campo']
        return kwargs

    def get_success_url(self, **kwargs):
        return reverse_lazy("gestione:detailcampo", kwargs={'pk': self.kwargs['pk_campo']})

# view per la visualizzazione dei dettagli di un campo
class CampoDetailView(DetailView):
    titolo = "Dettagli campo"
    context_object_name = 'campo'
    model = Campo
    template_name = "gestione/detailcampo.html"
    sconto = "0"
    
    
        
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if(self.request.user.id == None):
            self.sconto="0"
            return ctx
        p = ctx["object"]
        p=len(Prenotazione.objects.filter(utente_id=self.request.user.id))        
        if(p%3 == 0): 
            self.sconto="1" 
        elif((p-1)%3 == 0): 
            self.sconto="2" 
        elif((p+1)%3 == 0): 
            self.sconto="3"
        return ctx

        

# view per la creazione del form per selezionare una data
class SelezionaDataFormView(LoginRequiredMixin, FormView):
    template_name = 'gestione/create_entry.html'
    form_class = SelezionaDataForm
    
    
    def get_success_url(self):
        return reverse_lazy('gestione:aggiungiprenotazione', kwargs={'giornop': self.giorno, 'datap': self.date, 'pk_campop': self.kwargs['pk_campo']  })

    def form_valid(self, form):
        self.giorno=form.cleaned_data["date"].weekday()
        self.date=form.cleaned_data["date"]
        return super().form_valid(form)


# view per la creazione di una prenotazione
class CreatePrenotazioneView(LoginRequiredMixin, CreateView):
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


# view per la lista dei campi possedutti da un dirigente
class CampiSituationView(GroupRequiredMixin, ListView):
    group_required = ["Dirigenti"]
    model = Campo
    template_name = "gestione/lista_campi.html"

    def get_queryset(self):
        return Campo.objects.filter(utente_id=self.request.user)

# view per visualizzare le prentoazioni dei campi di un dirigente    
class PrenotazioniDirigenteView(GroupRequiredMixin, ListView):
    group_required = ["Dirigenti"]
    context_object_name = 'prenotazione'
    model = Prenotazione
    template_name = "gestione/situation.html"

    def get_queryset(self):

        return Prenotazione.objects.filter(ora__giorno__campo__utente=self.request.user)
            
    def get_context_data(self, **kwargs):
        context = super(PrenotazioniDirigenteView, self).get_context_data(**kwargs)
        return context


# view per visualizzazione delle proprie prenotazioni
class PrenotazioniView(LoginRequiredMixin, ListView ):
    context_object_name = 'prenotazione'
    model = Prenotazione
    template_name = "gestione/situation.html"

    def get_queryset(self):
            return Prenotazione.objects.filter(utente_id=self.request.user)
            
    def get_context_data(self, **kwargs):
        context = super(PrenotazioniView, self).get_context_data(**kwargs)
        context['oggi'] = date.today()
        return context

# view per comunicare l'esito di una prenotazione
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


# view per eliminare una prenotazione 
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

# view per eliminare un giorno
class EliminaGiornoView(GroupRequiredMixin, DetailView):
    group_required = ["Dirigenti"]
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

# view per eliminare un campo
class EliminaCampoView(GroupRequiredMixin, DetailView):
    group_required = ["Dirigenti"]
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

# fuzione per la ricerca dei campi
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

# view per lista lista dei campi filtrati per la ricerca
class CampoRicercaView(CampoListView):
    titolo = "La tua ricerca ha dato come risultato"

    def get_queryset(self):
        sstring = self.request.resolver_match.kwargs["sstring"] 
        cap = self.request.resolver_match.kwargs["cap"]

        
      
        qq = self.model.objects.filter(indirizzo__icontains=sstring) | self.model.objects.filter(giocatori__icontains=sstring)
        if (cap != "None"): qq = sorted(qq, key=lambda campi: campi.confronta_distanza(cap) )



        return qq
