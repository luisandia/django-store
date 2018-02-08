from django.db import models

# Create your models here.
class ItemCategorie(models.Model):
	item_id    = models.AutoField(primary_key = True)
	item_name  = models.CharField(max_length = 45)
	has_kardex = models.IntegerField()
	def __str__(self):
		return self.item_name