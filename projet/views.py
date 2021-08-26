from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context

from .models import Projet

def index(request):
    projet= Projet.objects.all()
    return render(request,"index.html",{"projet":projet})

def test(request):
    condition = request.GET.get("response")
    if condition=="oui":
        return HttpResponse("Vous etez tres satisfait! On est tres heureux pour vous!")
    else:
        return HttpResponse("On est desolée que vous n'etes pas satisfait!")





