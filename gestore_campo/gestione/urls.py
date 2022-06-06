from django.urls import path
from . import views
from django.views.generic.edit import CreateView


app_name = "gestione"

urlpatterns = [
    path('', views.gestione_home,  name="home"),
    path("listacampi/", views.CampoListView.as_view(),name="listacampi"),
]
