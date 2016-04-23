from django.shortcuts import render

# Create your views here.

def homepage(request):
    symptoms = Symptom.objects
    return render(request, 'space/homepage.html', {'pins' : symptoms})
    
def about(request):
    return render(request, 'space/about.html', {})