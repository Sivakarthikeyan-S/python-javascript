from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/hello.html")

def siva(request):
    return HttpResponse("Hello, Siva!")

def karthi(request):
    return HttpResponse("Hello, Karthi!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })