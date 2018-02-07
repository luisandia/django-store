from django.db import models

# Create your models here.
class unit_type(models.Model):
    id_unit_type = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name