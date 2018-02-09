from django.contrib import admin
from ..warehouse_.models import unit_type
from .models import Warehouse
from .models import WarehouseHasItem
# Register your models here.
admin.site.register(unit_type)
admin.site.register(Warehouse)
admin.site.register(WarehouseHasItem)
