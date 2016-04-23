from django.shortcuts import render, redirect

from .forms import SymptomForm


# Create your views here.

def homepage(request):
    return render(request, 'space/homepage.html', {})
    
def about(request):
    return render(request, 'space/about.html', {})
    
def report(request):
    if request.method == "POST":
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptom = form.save(commit=False)
            symptom.save()
            return redirect('homepage')
    else:
        form = SymptomForm()
    return render(request, 'space/report.html', {'form' : form })