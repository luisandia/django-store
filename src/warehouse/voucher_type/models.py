from django.db import models

# Create your models here.
class voucher_type(models.Model):
    id_voucher_type = models.AutoField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.name