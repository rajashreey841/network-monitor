from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'netmon/home.html')

def about(request):
    return render(request, 'netmon/about.html', {'title': "About"})