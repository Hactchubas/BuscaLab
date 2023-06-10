from django import forms
from .models import Report



class makeReport(forms.ModelForm):

    class Meta:
        model = Report
        fields = '__all__'

        labels = {
            "lab" : "Laboratory",
            "identifier": "Name",      
        }

        widgets = {
            'lab': forms.Select(attrs={
                "placeholder": "Laboratory",
            }),

            "category": forms.Select(attrs={
                "placeholder": "Category",
            }, choices =[
                ("computer","Computer"),
                ("equipament","Equipament"),
                ("software", "Software"),
                ("other", "Other")
            ]),

            'identifier': forms.TextInput(attrs={
                "placeholder": "Name",
            }),

            'problem': forms.Select(attrs={
                "placeholder": "Category",
            }, choices =[
                ("not_istalled","Not installed"),
                ("not_opennig","Doesn't open"),
                ("expired", "Expired"),
                ("other", "Other")
            ]),

            'description': forms.Textarea(attrs={
                "placeholder": "Description",
            }),

        }