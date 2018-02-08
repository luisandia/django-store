from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import voucher_type
from .forms import VoucherTypeForm
from django.urls import reverse_lazy
# Create your views here.
class ListVoucherType(ListView):
    model = voucher_type
    template_name = 'list_voucher_type.html'

class CreateVoucherType(CreateView):
    model = voucher_type
    form_class = VoucherTypeForm
    template_name = 'create_voucher_type.html'
    success_url = reverse_lazy("List_VoucherType")

class UpdateVoucherType(UpdateView):
    model = voucher_type
    form_class = VoucherTypeForm
    template_name = 'create_voucher_type.html'
    success_url = reverse_lazy("List_VoucherType")

class DeleteVoucherType(DeleteView):
    model = voucher_type
    template_name = 'delete_voucher_type.html'
    success_url = reverse_lazy("List_VoucherType")