from django.contrib import admin
from .models import ItemCategorie
from .models import Item
from .models import ExistenceType
# Register your models here.
admin.site.register(ItemCategorie)
admin.site.register(Item)
admin.site.register(ExistenceType)