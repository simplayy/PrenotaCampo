from django.urls import path
from . import views
from django.views.generic.edit import CreateView


app_name = "gestione"

urlpatterns = [
    path('', views.gestione_home,  name="home"),
    path("listacampi/", views.CampoListView.as_view(),name="listacampi"),
    path("detailcampo/<pk>/", views.CampoDetailView.as_view(), name="detailcampo"),
    path("aggiungicampo/",views.CreateCampoView.as_view(),name="aggiungicampo"),
    path("aggiungigiorno/",views.CreateGiornoView.as_view(),name="aggiungigiorno"),
    path("aggiungiora/<pk>/",views.CreateOraView.as_view(),name="aggiungiora")
]
