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
    path("aggiungirecensione/<pk_campo>/",views.CreateRecensioneView.as_view(),name="aggiungirecensione"),
    path("selezionadata/<pk_campo>/",views.SelezionaDataFormView.as_view(),name="selezionadata"),
    path("aggiungiprenotazione/<giornop>/<datap>/<pk_campop>/",views.CreatePrenotazioneView.as_view(),name="aggiungiprenotazione"),
    path("eliminaprenotazione/<pk>/",views.EliminaPrenotazioneView.as_view(),name="eliminaprenotazione"),
    path("eliminagiorno/<pk>/",views.EliminaGiornoView.as_view(),name="eliminagiorno"),
    path("eliminacampo/<pk>/",views.EliminaCampoView.as_view(),name="eliminacampo"),
    path("esitoprenotazione/<pk>/",views.EsitoPrenotazioneView.as_view(),name="esitoprenotazione"),
    path("situationc/",views.CampiSituationView.as_view(),name="situationc"),
    path("situation/",views.PrenotazioniView.as_view(),name="situation"),
    path("situationdirigente/",views.PrenotazioniDirigenteView.as_view(),name="situationdirigente"),
    path("ricerca/", views.search, name="cercacampo"),
    path("ricerca/<str:sstring>/<str:cap>/", views.CampoRicercaView.as_view(), name="ricerca_risultati"),
]
