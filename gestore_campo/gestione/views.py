from django.shortcuts import render

# Create your views here.


def gestione_home(request):
    return render(request,template_name="gestione/home.html")