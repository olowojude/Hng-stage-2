from django.db import models
from enum import Enum


class Calculations(Enum):
    addition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"


class Fields(models.Model):
    operation_type = models.CharField(
        max_length=50, choices=[(tag.name, tag.value) for tag in Calculations]
        )
    x= models.IntegerField()
    y= models.IntegerField()