from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

class CreateCampoForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "addcampo_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit","Aggiungi Campo"))

    class Meta:
        model = Campo
        fields = ["id","indirizzo","prezzo", "mq", "giocatori"]