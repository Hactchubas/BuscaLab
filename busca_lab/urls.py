from django.urls import path
from . import views

app_name = "buscalab"
urlpatterns = [
    path("",views.index, name="index"),
    path("<int:lab_id>", views.lab, name="lab"),
]