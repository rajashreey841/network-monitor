from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return "<h1>Network Monitor Home</h1>"