from django.test import TestCase

from django.test import TestCase

from .models import Campo, User
from .forms import CreateCampoForm

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



class CreateCampoFormTest(TestCase):

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

