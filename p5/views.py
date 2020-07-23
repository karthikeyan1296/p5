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

def fifth(request):
    return render(request,"directory/fifth.html",context={'a':"10",'b':"20"})

def urls_data(request,name):
    return HttpResponse("<h1>{}<h1>".format(name))

def urls_data1(request,ab):   #adding two no. by using single argument(ab)
    a=ab.split(" ")
    sum=int(a[0])+int(a[1])
    return HttpResponse(str(sum))

def urls_data2(request,c,d):   #adding two no. by using two argument(c,d)
    sum=int(c)+int(d)
    return HttpResponse(str(sum))

def urls_data3(request,greater):
    g=greater.split(" ")
    if int(g[0]) > int(g[1]):
        return HttpResponse(str(g[0]))

    else:
        return HttpResponse(str(g[1]))

def urls_data4(request,string):
    vowels = 'aeiouAEIOU'
    vow = 0
    con = 0
    for i in string:
        if i in vowels:
            vow+=1
        else:
            con+=1
    return render(request,"directory/vowel.html",context={'v':vow,'c':con})