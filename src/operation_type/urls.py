#from django.conf.urls import url
from django.urls import path
from .views import (
    ListOperationType,
    CreateOperationType,
    UpdateOperationType,
    DeleteOperationType,
)

urlpatterns = [
    path('list',ListOperationType.as_view(),name="List_OperationType"),
    path('create',CreateOperationType.as_view(),name="Create_OperationType"),
    path('update/<int:pk>/', UpdateOperationType.as_view(), name="Update_OperationType"),
    path('delete/<int:pk>/', DeleteOperationType.as_view(), name="Delete_OperationType"),
]