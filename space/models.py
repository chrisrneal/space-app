from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class Symptom(models.Model):
    symptomName = models.CharField(max_length=200)
    intensity = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    time = models.DateTimeField(default=timezone.now)
    locLat = models.FloatField()
    locLong = models.FloatField()
    streetaddress = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    postal = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)

    
    def __str__(self):
        return self.symptomName

