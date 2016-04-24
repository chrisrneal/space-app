from django.shortcuts import render, redirect

from .forms import SymptomForm, CityForm
from .models import Symptom
import urllib, json

googAPIkey = 'AIzaSyCG8ODmR1HGc5yglzEeBix2EqzrlbCg7F8'

def geocode(location):
    output = "json"
    request = "https://maps.googleapis.com/maps/api/geocode/%s?address=%s&key=%s" % (output, location, googAPIkey)
    data = urllib.urlopen(request).read()
    data = json.loads(data)
    if data["status"] == "OK":
        return {'lat': data["results"][0]["geometry"]["location"]["lat"], 'lng': data["results"][0]["geometry"]["location"]["lng"]}
    else:
        return {'lat': 43.659705, 'lng': -79.4955992}
# Create your views here.

def getSymptomList(symptoms):
    retVal = []
    for n in symptoms:
        if n.symptomName not in retVal:
            retVal.append(n.symptomName)
    return retVal

def homepage(request):
    pins = Symptom.objects.all()
    symptomList = getSymptomList(pins)
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            city = city.replace(" ", "+")
            state = state.replace(" ", "+")
            coords = geocode(city+","+state)
    else:
        coords = {'lat': 43.659705, 'lng': -79.4955992}
        form = CityForm()
    
    return render(request, 'space/homepage.html', { 'pins' : pins, 'symptomList' : symptomList, 'form':form, 'lat': coords['lat'], 'lng': coords['lng'] })
    
def about(request):
    return render(request, 'space/about.html', {})
    
def report(request):
    if request.method == "POST":
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptom = form.save(commit=False)
            symptom.setLongAndLat()
            symptom.save()
            return redirect('homepage')
    else:
        form = SymptomForm()
    return render(request, 'space/report.html', {'form' : form })
    
def logs(request): 
    symptoms = Symptom.objects.all()
    symptomList = getSymptomList(symptoms)
    
    return render(request, 'space/logs.html', {'symptoms' : symptoms, 'symptomList' : symptomList })