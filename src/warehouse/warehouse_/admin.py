from django.contrib import admin

from .models import (
    Warehouse,
    WarehouseHasItem,
    UnitType,
    VoucherType,
    OperationType
)
# Register your models here.
admin.site.register(UnitType)
admin.site.register(VoucherType)
admin.site.register(OperationType)
admin.site.register(Warehouse)
admin.site.register(WarehouseHasItem)
