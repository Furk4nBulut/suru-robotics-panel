from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse("<h1>Suru Robotics</h1>")
# Create your views here.
