from django.shortcuts import render
from .models import PC_model, Software, Lab, Quantity, Equipament, Report
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
def index(request):
    return render(request, "busca_lab/index.html",{
        "labs": Lab.objects.all(),
    })

def lab(request, lab_id):    
    laboratorie = Lab.objects.get(pk = lab_id)    
    
    if not request.user.is_authenticated:
        return render(request, "busca_lab/lab.html",{
            "lab": laboratorie, 
            "models": Quantity.objects.filter(lab = laboratorie).all(),
            "softwares": laboratorie.softwares.all(),

        })
    
    return render(request, "busca_lab/adm_index.html",{
        "labs": Lab.objects.all(),
        "lab": laboratorie, 
        "models": Quantity.objects.filter(lab = laboratorie).all(),
        "softwares": laboratorie.softwares.all(),  
        "equipaments": laboratorie.equipaments.all(), 
        "reports": Report.objects.all(),
    })

def login(request):    
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
            # return HttpResponseRedirect(reverse("login"))
        else:
            return render(request, "busca_lab/login.html",{
                "message": "Invalid credentials.",
            })
    
    if not request.user.is_authenticated:
        return render(request, "busca_lab/login.html")
    lab = Lab.objects.get(id=1)
    return render(request, "busca_lab/adm_index.html",{
        "software": lab.softwares.all(), 
        "model": Quantity.objects.filter(lab = 1).all(),
        "labs": Lab.objects.all(),
        "softwares": Software.objects.all(),
        "models": Quantity.objects.all(),
    })

def logout(request):
    auth_logout(request)
    return render(request, "busca_lab/login.html",{
        "message": "Logged out."
    })

def reportPage(request):
    return render(request, "busca_lab/report.html")
