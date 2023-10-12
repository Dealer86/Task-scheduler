from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("<h1>Home</h1>")
    return render(request, "tasks/home.html")


def about(request):
    # return HttpResponse("<h1>About</h1>")
    return render(request, "tasks/about.html")
