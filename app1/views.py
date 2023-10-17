from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello.html")


def index1(request):
    return render(request, "hello.html")
