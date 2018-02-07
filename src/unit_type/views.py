from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
    DeleteView,
    UpdateView
)
from .models import unit_type
from .forms import UnitTypeForm
from django.urls import reverse_lazy
# Create your views here.
class ListUnitType(ListView):
    model = unit_type
    template_name = 'list_unit_type.html'

class CreateUnitType(CreateView):
    model = unit_type
    form_class = UnitTypeForm
    template_name = 'create_unit_type.html'
    success_url = reverse_lazy("List_UnitType")

class UpdateUnitType(UpdateView):
    model = unit_type
    form_class = UnitTypeForm
    template_name = 'create_unit_type.html'
    success_url = reverse_lazy("List_UnitType")

class DeleteUnitType(DeleteView):
    model = unit_type
    template_name = 'delete_unit_type.html'
    success_url = reverse_lazy("List_UnitType")