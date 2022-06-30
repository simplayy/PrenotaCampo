import datetime
from django.test import TestCase
from django.test import TestCase

from .models import Campo, User
from .forms import CreateCampoForm, SelezionaDataForm

# test sui modelli
class ClassModelTest(TestCase):

    @classmethod
    # setup di un campo oggetto usato in tutti i metodi
    def setUpTestData(cls):
        Campo.objects.create(indirizzo='via test 13', prezzo=9, mq=60, giocatori=7, cap="41126")

    # esempio di test della label di indirizzo 
    def test_indirizzo_label(self):
        campo = Campo.objects.get(id=1)
        field_label = campo._meta.get_field('indirizzo').verbose_name
        self.assertEqual(field_label, 'indirizzo')

    # esempio di test sulla massima lunghezza di indirizzo
    def test_indirizzo_max_length(self):
        campo = Campo.objects.get(id=1)
        max_length = campo._meta.get_field('indirizzo').max_length
        self.assertEqual(max_length, 200)

    # esempio di test sull' __str__ dell'oggetto campo
    def test_object_campo_str(self):
        campo = Campo.objects.get(id=1)
        expected_object_name = campo.indirizzo + " a "+ str(campo.giocatori)
        self.assertEqual(str(campo), expected_object_name)

    # test sulla propieta' caparra del campo
    def test_object_campo_caparra(self):
        campo = Campo.objects.get(id=1)
        self.assertEqual(campo.caparra, 25)

    # test sulla propieta' lat del campo
    def test_object_campo_lat(self):
        campo = Campo.objects.get(id=1)
        self.assertEqual(campo.lat, 44.64600008)

    # test sulla propieta' lng del campo
    def test_object_campo_lat(self):
        campo = Campo.objects.get(id=1)
        self.assertEqual(campo.lng, 10.92615487)

    # test sulla propieta' comune del campo
    def test_object_campo_comune(self):
        campo = Campo.objects.get(id=1)
        self.assertEqual(campo.comune, "Modena")


# test sui form
class FormTest(TestCase):

    @classmethod
    # setup di un campo oggetto usato in tutti i metodi
    def setUpTestData(cls):
        User.objects.create(username="foo", password="bar")
        Campo.objects.create(indirizzo='via test 13', prezzo=9, mq=60, giocatori=7, cap="41126", utente=User.objects.get(id=1))

    # esempio test che la label di Indirizzo sia Indirizzo
    def test_CreateCampoForm_field_label(self):
        form = CreateCampoForm(user= User.objects.get(id=1))
        print(form.fields['indirizzo'].label)
        self.assertTrue(form.fields['indirizzo'].label == 'Indirizzo')

    # esempio test che controllo che il valore di deafult dei mq sia 90
    def test_CreateCampoForm_defaultvalue(self):
        form = CreateCampoForm(user= User.objects.get(id=1))
        self.assertTrue(form.fields["mq"].initial == 90)

    # test che verifica l'inserimento di una prenotazione con data nel passato
    def test_aggiungiprenotazione_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = SelezionaDataForm(data={'date': date})
        self.assertFalse(form.is_valid())

    # test che verifica l'inserimento di una prenotazione con data nel futuro
    def test_aggiungiprenotazione_form_date_in_past(self):
        date = datetime.date.today() + datetime.timedelta(days=1)
        form = SelezionaDataForm(data={'date': date})
        self.assertTrue(form.is_valid())


# test sulle view
class ViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create 13 campi for pagination tests
        number_of_campi = 13
        User.objects.create(username="foo", password="bar")
        
        for campo_id in range(number_of_campi):
            Campo.objects.create(indirizzo= str(campo_id), prezzo=9, mq=60, giocatori=7, cap="41126", utente=User.objects.get(id=1))


    # test che verifica se la pagina listacmpi e' correttamente visualizzata
    def test_view_url_exists_at_desired_location_list(self):
        response = self.client.get('/gestione/listacampi/')
        self.assertEqual(response.status_code, 200)

     # test che verifica se la pagina la pagina dettagli di un campo e' correttamente visualizzata
    def test_view_url_exists_at_desired_location_detail(self):
        response = self.client.get('/gestione/detailcampo/1/')
        self.assertEqual(response.status_code, 200)

    # test che verifica che sia usato il template corretto
    def test_view_uses_correct_template(self):
        response = self.client.get('/gestione/listacampi/')
        self.assertTemplateUsed(response, 'gestione/lista_campi.html')

    # test che verifica che siano visualizzati tutti e 13 i campi
    def test_pagination_is_ten(self):
        response = self.client.get('/gestione/listacampi/')
        self.assertEqual(len(response.context['campo_list']), 13)

    # test che verifica che se non sono loggato non visualizzo la pagina per selezionare la data
    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/gestione/selezionadata/1/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/'))

  # test che verifica che se sono loggato ma non ho i permessi non visualizzo la pagina
    def test_forbidden_if_logged_in_but_not_correct_permission(self):
        login = self.client.login(username='foo', password='bar')
        response = self.client.get('/gestione/aggiungicampo/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/'))