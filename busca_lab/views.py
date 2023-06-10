from django.shortcuts import render, redirect
from .models import PC_model, Software, Lab, Quantity, Equipament, Report
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .forms import makeReport


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

    make_report_data = request.session.get('make_report_data', None)
    form = makeReport(make_report_data)

    return render(request, 'busca_lab/report.html',{
        "form" : form,
        "labs": Lab.objects.all(),
    })

def reportSend(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['make_report_data'] = POST
    form = makeReport(request.POST)

    return redirect('buscalab:report')
   

def rulesPage(request):
    return render(request, "busca_lab/rules.html")
