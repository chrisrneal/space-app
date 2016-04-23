from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'space/homepage.html', {})
    
def about(request):
    return render(request, 'space/about.html', {})
    
def report(request):
    return render(request, 'space/report.html', {})