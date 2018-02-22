from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import (
    UnitType,
    OperationType,
    VoucherType,
    Warehouse,
)

from .forms import (
    UnitTypeForm,
    OperationTypeForm,
    VoucherTypeForm,
    WarehouseForm,
)
# Create your views here.


def index(request):
    return HttpResponse("Demo index.")


# UnitType views
class ListUnitType(ListView):
    model = UnitType
    template_name = 'warehouse_templates/unit_type_templates/list_unit_type.html'


class CreateUnitType(CreateView):
    model = UnitType
    form_class = UnitTypeForm
    template_name = 'warehouse_templates/unit_type_templates/create_unit_type.html'
    success_url = reverse_lazy('warehouse_templates:List_UnitType')


class UpdateUnitType(UpdateView):
    model = UnitType
    form_class = UnitTypeForm
    template_name = 'warehouse_templates/unit_type_templates/create_unit_type.html'
    success_url = reverse_lazy("warehouse_templates:List_UnitType")


class DeleteUnitType(DeleteView):
    model = UnitType
    template_name = 'warehouse_templates/unit_type_templates/delete_unit_type.html'
    success_url = reverse_lazy("warehouse_templates:List_UnitType")


# OperationType views
class ListOperationType(ListView):
    model = OperationType
    template_name = 'warehouse_templates/operation_type_templates/list_operation_type.html'


class CreateOperationType(CreateView):
    model = OperationType
    form_class = OperationTypeForm
    template_name = 'warehouse_templates/operation_type_templates/create_operation_type.html'
    success_url = reverse_lazy("warehouse_templates:List_OperationType")


class UpdateOperationType(UpdateView):
    model = OperationType
    form_class = OperationTypeForm
    template_name = 'warehouse_templates/operation_type_templates/create_operation_type.html'
    success_url = reverse_lazy("warehouse_templates:List_OperationType")


class DeleteOperationType(DeleteView):
    model = OperationType
    template_name = 'warehouse_templates/operation_type_templates/delete_operation_type.html'
    success_url = reverse_lazy("warehouse_templates:List_OperationType")


# VoucherType views
class ListVoucherType(ListView):
    model = VoucherType
    template_name = 'warehouse_templates/voucher_type_templates/list_voucher_type.html'


class CreateVoucherType(CreateView):
    model = VoucherType
    form_class = VoucherTypeForm
    template_name = 'warehouse_templates/voucher_type_templates/create_voucher_type.html'
    success_url = reverse_lazy("warehouse_templates:List_VoucherType")


class UpdateVoucherType(UpdateView):
    model = VoucherType
    form_class = VoucherTypeForm
    template_name = 'warehouse_templates/voucher_type_templates/create_voucher_type.html'
    success_url = reverse_lazy("warehouse_templates:List_VoucherType")


class DeleteVoucherType(DeleteView):
    model = VoucherType
    template_name = 'warehouse_templates/voucher_type_templates/delete_voucher_type.html'
    success_url = reverse_lazy("warehouse_templates:List_VoucherType")


# Warehouse views
class ListWarehouse(ListView):
    model = Warehouse
    template_name = 'warehouse_templates/warehouse_templates_/list_warehouse.html'


class CreateWarehouse(CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'warehouse_templates/warehouse_templates_/create_warehouse.html'
    success_url = reverse_lazy("warehouse_templates:List_Warehouse")


class UpdateWarehouse(UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'warehouse_templates/warehouse_templates_/create_warehouse.html'
    success_url = reverse_lazy("warehouse_templates:List_Warehouse")


class DeleteWarehouse(DeleteView):
    model = Warehouse
    template_name = 'warehouse_templates/warehouse_templates_/delete_warehouse.html'
    success_url = reverse_lazy("warehouse_templates:List_Warehouse")