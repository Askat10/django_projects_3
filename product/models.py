from django.db import models

# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=100)
    square = models.DecimalField(max_digits=7, decimal_places=2)
    people_quantity = models.IntegerField(max_length=9)
    