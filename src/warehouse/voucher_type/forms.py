# -*- coding: utf-8 -*-
from django import forms
from .models import voucher_type

class VoucherTypeForm(forms.ModelForm):
    class Meta:
        model = voucher_type
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