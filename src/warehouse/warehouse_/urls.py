from django.urls import path, include

from . import views
from .views import (
    ListUnitType,
    CreateUnitType,
    UpdateUnitType,
    DeleteUnitType,

    ListOperationType,
    CreateOperationType,
    UpdateOperationType,
    DeleteOperationType,

    ListVoucherType,
    CreateVoucherType,
    UpdateVoucherType,
    DeleteVoucherType,
)

app_name = 'warehouse_templates'

urlpatterns = [
    path('', views.index, name='index'),
    #UnitType urls
    path('unit_type/list', ListUnitType.as_view(), name="List_UnitType"),
    path('unit_type/create', CreateUnitType.as_view(), name="Create_UnitType"),
    path('unit_type/update/<int:pk>/', UpdateUnitType.as_view(), name="Update_UnitType"),
    path('unit_type/delete/<int:pk>/', DeleteUnitType.as_view(), name="Delete_UnitType"),
    #OperationType urls
    path('operation_type/list',ListOperationType.as_view(),name="List_OperationType"),
    path('operation_type/create',CreateOperationType.as_view(),name="Create_OperationType"),
    path('operation_type/update/<int:pk>/', UpdateOperationType.as_view(), name="Update_OperationType"),
    path('operation_type/delete/<int:pk>/', DeleteOperationType.as_view(), name="Delete_OperationType"),
    #VoucherType urls
    path('voucher_type/list',ListVoucherType.as_view(),name="List_VoucherType"),
    path('voucher_type/create',CreateVoucherType.as_view(),name="Create_VoucherType"),
    path('voucher_type/update/<int:pk>/', UpdateVoucherType.as_view(), name="Update_VoucherType"),
    path('voucher_type/delete/<int:pk>/', DeleteVoucherType.as_view(), name="Delete_VoucherType"),
    # path('unit_type_templates/', include('warehouse_templates.unit_type_templates.urls')),
    # path('operation_type/', include('warehouse_templates.operation_type.urls')),
    # path('voucher_type/', include('warehouse_templates.voucher_type.urls')),
]