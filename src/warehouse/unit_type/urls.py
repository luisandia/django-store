#from django.conf.urls import url
from django.urls import path
from .views import (
    ListUnitType,
    CreateUnitType,
    UpdateUnitType,
    DeleteUnitType,
)

urlpatterns = [
    path('list', ListUnitType.as_view(), name="List_UnitType"),
    path('create', CreateUnitType.as_view(), name="Create_UnitType"),
    path('update/<int:pk>/', UpdateUnitType.as_view(), name="Update_UnitType"),
    path('delete/<int:pk>/', DeleteUnitType.as_view(), name="Delete_UnitType"),
]