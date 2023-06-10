from django.urls import path
from . import views

app_name = "buscalab"
urlpatterns = [
    path("",views.index, name="index"),
    path("<int:lab_id>", views.lab, name="lab"),
    path("login", views.login, name="login"),
    path("logout",views.logout, name="logout"),

    path("report", views.reportPage, name="report"),
    path("report/create", views.reportSend, name="reportCreate"),
    path("rules", views.rulesPage, name="rules")
]