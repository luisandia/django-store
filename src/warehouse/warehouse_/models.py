from django.db import models
from item.item_ import models as item_models
# Create your models here.

class unit_type(models.Model):
	id_unit_type = models.AutoField(primary_key=True)
	code         = models.CharField(max_length=45)
	name         = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Warehouse(models.Model):
	warehouse_id = models.AutoField(primary_key=True)
	name         = models.CharField(max_length = 45)
	description  = models.CharField(max_length = 45)
	def __str__(self):
		return self.name

class WarehouseHasItem(models.Model):
	warehouse = models.ForeignKey(Warehouse, on_delete = models.CASCADE)
	item      = models.ForeignKey(item_models.Item, on_delete = models.CASCADE, null = True)
	is_deleted   = models.IntegerField()