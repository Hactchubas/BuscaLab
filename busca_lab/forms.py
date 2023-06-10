from django import forms
from .models import Report

class makeReport(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'