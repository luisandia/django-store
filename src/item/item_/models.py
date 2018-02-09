from django.db import models

# Create your models here.
class ExistenceType(models.Model):
	existence_type_id = models.AutoField(primary_key = True)
	code              = models.CharField(max_length = 45)
	name              = models.CharField(max_length = 45)
	def __str__(self):
		return self.name
		
class ItemCategorie(models.Model):
	item_category_id = models.AutoField(primary_key = True)
	category_name    = models.CharField(max_length = 45)
	has_kardex       = models.IntegerField()
	def __str__(self):
		return self.item_name


class Item(models.Model):
	item_id        = models.AutoField(primary_key = True)
	item_name      = models.CharField(max_length = 40)
	description    = models.CharField(max_length = 48)
	category_id    = models.ForeignKey(ItemCategorie, on_delete = models.CASCADE)
	existence_type = models.ForeignKey(ExistenceType,on_delete = models.CASCADE) 
	def __str__(self):
		return self.item_name