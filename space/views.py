from django.shortcuts import render, redirect

from .forms import SymptomForm
from .models import Symptom


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
    return render(request, 'space/homepage.html', { 'pins' : pins, 'symptomList' : symptomList})
    
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