from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_page(request):
    # return HttpResponse("I am a Django Developer!!!")
    return render(request, "home/base.html")


def profiles(request):
    profiles = [
        {"name": "Karan", "age": 22},
        {"name": "Arjun", "age": 19},
        {"name": "Ranbir", "age": 23},
        {"name": "Suraj", "age": 17}
    ]
    return render(request, "home/profiles.html", context={"page": "profiles", "profiles": profiles})


def about(request):
    context = {"page": "about"}
    return render(request, "home/about.html", context=context)
