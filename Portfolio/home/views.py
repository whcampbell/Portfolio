from django.shortcuts import render
from django.http import HttpResponse

def welcome(request) :
    return render(request, 'home/welcome.html')

def about(request) :
    return render(request, 'home/about.html')
# Create your views here.
