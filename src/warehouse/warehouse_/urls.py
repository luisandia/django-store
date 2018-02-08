from django.urls import path, include

from . import views

app_name = 'warehouse'

urlpatterns = [
    path('', views.index, name='index'),
    path('unit_type/', include('warehouse.unit_type.urls')),
    path('operation_type/', include('warehouse.operation_type.urls')),
    path('voucher_type/', include('warehouse.voucher_type.urls')),
]