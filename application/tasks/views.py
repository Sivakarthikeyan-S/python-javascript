from django.shortcuts import render

tasks = ["one", "two", "three", "four", "five"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })