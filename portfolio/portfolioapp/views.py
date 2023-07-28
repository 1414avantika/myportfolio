from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
def use(request):
    return render(request,'home.html')


def test(request):
    return render(request,"about.html")

def cat(request):
    return render(request,'contact.html')

def dog(request):
    return render(request,'resume.html')

def holl(request):
    return render(request, 'portfolio.html')

def moll(request):
    return render(request, 'services.html')

def fall(request):
    return render(request, 'home.html')