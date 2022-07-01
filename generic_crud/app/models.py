from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    domain = models.CharField(max_length=30)