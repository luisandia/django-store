from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import operation_type
from .forms import OperationTypeForm
from django.urls import reverse_lazy
# Create your views here.
class ListOperationType(ListView):
    model = operation_type
    template_name = 'list_operation_type.html'

class CreateOperationType(CreateView):
    model = operation_type
    form_class = OperationTypeForm
    template_name = 'create_operation_type.html'
    success_url = reverse_lazy("List_OperationType")

class UpdateOperationType(UpdateView):
    model = operation_type
    form_class = OperationTypeForm
    template_name = 'create_operation_type.html'
    success_url = reverse_lazy("List_OperationType")

class DeleteOperationType(DeleteView):
    model = operation_type
    template_name = 'delete_operation_type.html'
    success_url = reverse_lazy("List_OperationType")