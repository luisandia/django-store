from django.db import models

# Create your models here.
class operation_type(models.Model):
    id_type_operation = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.name