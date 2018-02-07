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
from django.core.urlresolvers import  reverse_lazy
# Create your views here.
class ListUnitType(ListView):
    model = unit_type
    template_name =

class CreateUnitType(CreateView):
    model = unit_type
    form_class = UnitTypeForm
    template_name =
    success_url = reverse_lazy("")

class UpdateUnitType(UpdateView):
    model = unit_type
    form_class = UnitTypeForm
    template_name =
    success_url = reverse_lazy("")

class DeleteUnitType(DeleteView):
    model = unit_type
    template_name =
    success_url = reverse_lazy("")