from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=255)


class Vaccination(models.Model):
    rut = models.CharField(max_length=10)
    dose = models.FloatField()
    date = models.DateField()
    drug = models.ForeignKey(Drug, related_name='drug', on_delete=models.CASCAD