from django.shortcuts import render
from .models import PC_model, Software, Lab, Quantity
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "busca_lab/index.html",{
        "labs": Lab.objects.all(),
    })

def lab(request, lab_id):
    laboratorie = Lab.objects.get(pk = lab_id)    
    
    return render(request, "busca_lab/lab.html",{
        "lab": laboratorie, 
        "models": Quantity.objects.filter(lab = laboratorie).all(),
        "softwares": laboratorie.softwares.all(),   
    })