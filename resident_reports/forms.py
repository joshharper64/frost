from django import forms

from .models import Report

class ReportForm(forms.Modelform):
    class Meta:
        model = Report
        fields = ['text']
        labels = {'text': ''}
