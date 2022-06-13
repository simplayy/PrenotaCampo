from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from .models import *

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
        



    