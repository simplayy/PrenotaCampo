from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.


def gestione_home(request):
    return render(request,template_name="gestione/home.html")

