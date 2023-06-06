from django.shortcuts import render

def index(request) :
    return render(request, 'projects/index.html')

def snake(request) :
    return render(request, 'projects/snake.html')

# Create your views here.
