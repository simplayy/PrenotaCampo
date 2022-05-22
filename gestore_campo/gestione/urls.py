from django.urls import path
from . import views


app_name = "gestione"

urlpatterns = [
    path('', views.gestione_home,  name="home")
]
