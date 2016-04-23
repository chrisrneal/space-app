from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Symptom(models.Model):
    symptomName = models.CharField(max_length=200)
    intensity = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    time = models.DateTimeField()
    locLat = models.FloatField()
    locLong = models.FloatField()
    
    def __str__(self):
        return self.symptomName

