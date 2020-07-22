from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>WELCOME TO THE PROJECT P5</MARQUEE>")

def first(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html")
