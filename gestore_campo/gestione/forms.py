from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import redirect
import datetime


class CreateCampoForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "addcampo_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit","Aggiungi Campo"))

    class Meta:
        model = Campo
        fields = ["indirizzo", "prezzo", "mq", "giocatori"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreateCampoForm, self).__init__(*args, **kwargs)
        self.instance.utente=user


class CreateGiornoForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "addgiorno_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit","Aggiungi Giorno"))

    class Meta:
        model = Giorno
        fields = ["giorno", "campo"]

    def __init__(self, *args, **kwargs):
        
        pk_campo = kwargs.pop('pk_campo')
        user = kwargs.pop('user')
        super(CreateGiornoForm, self).__init__(*args, **kwargs)
        self.fields['campo']=forms.ModelChoiceField(queryset=Campo.objects.filter(utente=user))
        self.fields['campo'].initial = pk_campo
        self.fields['campo'].disabled = True

class CreateOraForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "addora_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit","Aggiungi Ora"))

    class Meta:
        model = Ora
        fields = ["ora", "giorno"]

    def __init__(self, *args, **kwargs):

        pk_giorno = kwargs.pop('pk_giorno')
        pk_campo = kwargs.pop('pk_campo')
        
        
        super(CreateOraForm, self).__init__(*args, **kwargs)
        self.fields['giorno']=forms.ModelChoiceField(queryset=Giorno.objects.filter(campo_id=pk_campo))
        self.fields['giorno'].initial = pk_giorno
        self.fields['giorno'].disabled = True
        

class CreateRecensioneForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "addrecensione_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit","Aggiungi Recensione"))
    class Meta:
        model = Recensione
        fields = ["utente", "campo", "descrizione", "stelle"]
        labels  = {
            'stelle': ('Stelle (1-5)'),
        }
       
    def __init__(self, *args, **kwargs):
        pk_campo = kwargs.pop('pk_campo')

        utente = kwargs.pop('utente')
        
        
        
        super(CreateRecensioneForm, self).__init__(*args, **kwargs)
        self.fields['utente'].initial = utente
        self.fields['utente'].disabled = True

        self.fields['campo'].initial = pk_campo
        self.fields['campo'].disabled = True

    def clean_campo(self):
        if (len(Prenotazione.objects.filter(utente_id=self.cleaned_data['utente']))==0):
            raise forms.ValidationError("Negro di merda!")
        return self.cleaned_data['campo']

class SelezionaDataForm(forms.Form):
    helper = FormHelper()
    helper.form_id = "verificadata_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit","Vedi Orari"))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Non puoi selezionare una data nel passato!")
        return date

class CreatePrenotazioneForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "addpren_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit","Aggiungi Prenotazione"))

    class Meta:
        model = Prenotazione
        fields = ["data", "ora"]

    def __init__(self, *args, **kwargs):

        data = kwargs.pop('datap')
        giorno = kwargs.pop('giornop')
        pk_campo = kwargs.pop('pk_campop')
        user = kwargs.pop('user')
        try:
            pk_giorno=Giorno.objects.filter(campo_id=pk_campo, giorno=giorno).values_list('pk', flat=True)[0]
        except:
            pk_giorno=None
        
        super(CreatePrenotazioneForm, self).__init__(*args, **kwargs)
        self.fields['ora']=forms.ModelChoiceField(queryset=Ora.objects.filter(giorno_id=pk_giorno))
        self.fields['data'].initial=data
        self.fields['data'].disabled = True
        self.instance.utente=user

    
        
        
class SearchForm(forms.Form):

    helper = FormHelper()
    helper.form_id = "search_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit","Cerca"))
    caratteristiche = forms.CharField(label="Cerca qualcosa",  max_length=400, required=True)
    cap = forms.CharField(label="CAP",  max_length=400, required=False)