# -*- coding: utf-8 -*-
from django import forms
from .models import operation_type

class OperationTypeForm(forms.ModelForm):
    class Meta:
        model = operation_type
        fields = [
            'name',
            'description'
        ]

        labels = {
            'name':'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
