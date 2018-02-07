#from django.conf.urls import url
from django.urls import path
from .views import (
    ListVoucherType,
    CreateVoucherType,
    UpdateVoucherType,
    DeleteVoucherType,
)

urlpatterns = [
    path('list',ListVoucherType.as_view(),name="List_VoucherType"),
    path('create',CreateVoucherType.as_view(),name="Create_VoucherType"),
    path('update/<int:pk>/', UpdateVoucherType.as_view(), name="Update_VoucherType"),
    path('delete/<int:pk>/', DeleteVoucherType.as_view(), name="Delete_VoucherType"),
]