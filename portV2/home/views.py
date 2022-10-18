from django.shortcuts import render
from .models import Projekt

def index(request):
    arg = dict()

    progekts = Projekt.objects.all()
    arg['progekts'] = progekts
    print(progekts[0])
    arg['kolvo'] = len(progekts)
    progs = dict()
    arg['kol_list'] = [0]
    for i in range(len(progekts)):
        progs[i] = progekts[i]
    return render(request, "index.html",arg)