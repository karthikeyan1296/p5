from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>WELCOME TO THE PROJECT P5</MARQUEE>")

def first(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html",context={'data':"RSK",'name':"karthi"})

def fourth(request):
    fruits=['apple','orange','kiwi','watermelon','musk melon']
    return render(request,"directory/fourth.html",{'fruits':fruits})