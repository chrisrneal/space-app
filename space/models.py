from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
import urllib
import json

googAPIkey = 'AIzaSyCG8ODmR1HGc5yglzEeBix2EqzrlbCg7F8'

class Symptom(models.Model):
    symptomName = models.CharField(max_length=200)
    intensity = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    time = models.DateTimeField(default=timezone.now)
    locLat = models.FloatField(blank=True)
    locLong = models.FloatField(blank=True)
    streetaddress = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    postal = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)

    def setLongAndLat(self):
        addrString = "%s, %s, %s, %s, %s" % (self.streetaddress, self.city, self.province, self.postal, self.country)
        addrString = addrString.replace(" ", "+")
        if not self.locLat or not self.locLong:
            latlng = self.geocode(addrString)
            latlng = latlng.split(',')
            self.locLat = latlng[0]
            self.locLong = latlng[1]
        
        
    def geocode(self, location):
        output = "json"
        request = "https://maps.googleapis.com/maps/api/geocode/%s?address=%s&key=%s" % (output, location, googAPIkey)
        data = urllib.urlopen(request).read()
        data = json.loads(data)
        if data["status"] == 'OK':
            return "%s,%s" % (data["results"][0]["geometry"]["location"]["lat"], data["results"][0]["geometry"]["location"]["lng"])
        else:
            return ','
        
    def __str__(self):
        return self.symptomName

