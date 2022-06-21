from django.urls import path
from . import views
from django.views.generic.edit import CreateView


app_name = "gestione"

urlpatterns = [
    path('', views.gestione_home,  name="home"),
    path("listacampi/", views.CampoListView.as_view(),name="listacampi"),
    path("detailcampo/<pk>/", views.CampoDetailView.as_view(), name="detailcampo"),
    path("aggiungicampo/",views.CreateCampoView.as_view(),name="aggiungicampo"),
    path("aggiungigiorno/<pk_campo>/",views.CreateGiornoView.as_view(),name="aggiungigiorno"),
    path("aggiungiora/<pk_campo>/<pk_giorno>/",views.CreateOraView.as_view(),name="aggiungiora"),
    path("selezionadata/<pk_campo>/",views.SelezionaDataFormView.as_view(),name="selezionadata"),
    path("aggiungiprenotazione/<giornop>/<datap>/<pk_campop>/",views.CreatePrenotazioneView.as_view(),name="aggiungiprenotazione"),
    path("eliminaprenotazione/<pk>/",views.EliminaPrenotazioneView.as_view(),name="eliminaprenotazione"),
    path("situationc/",views.CampiSituationView.as_view(),name="situationc"),
    path("situation/",views.PrenotazioniView.as_view(),name="situation")
]
