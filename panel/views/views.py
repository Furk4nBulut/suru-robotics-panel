from django.shortcuts import render
from django.http import HttpResponse

def first(request):


    return render(request,'index.ejs')

# Create your views here.
