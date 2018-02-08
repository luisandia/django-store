# -*- coding: utf-8 -*-
from django import forms
from .models import unit_type

class UnitTypeForm(forms.ModelForm):
    class Meta:
        model = unit_type
        fields = [
            'code',
            'name',
        ]

        labels = {
            'code':'Codigo',
            'name':'Nombre',
        }

        widgets = {
            'code':forms.TextInput(attrs={'class': 'form-control'}),
            'name':forms.TextInput(attrs={'class': 'form-control'}),
        }
