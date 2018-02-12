# -*- coding: utf-8 -*-
from django import forms
from .models import (
    UnitType,
    OperationType,
    VoucherType,
)

class UnitTypeForm(forms.ModelForm):
    class Meta:
        model = UnitType
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

class OperationTypeForm(forms.ModelForm):
    class Meta:
        model = OperationType
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


class VoucherTypeForm(forms.ModelForm):
    class Meta:
        model = VoucherType
        fields = [
            'code',
            'name',
            'description'
        ]

        labels = {
            'code':'Codigo',
            'name':'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'code':forms.NumberInput(attrs={'class': 'form-control'}),
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }