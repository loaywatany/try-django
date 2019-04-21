from django.http import HttpResponse
from django.shortcuts import render



def home_page(request):
    my_title = "hello there ...."

    return render(request, "hello_world.html", {"title": my_title})

def about_page(request):
    return render(request, "about.html", {"title": "About us"})

def contact_page(request):
    return render(request, "contact.html", {"title": "Contact us"})