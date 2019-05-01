from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm

def home_page(request):
    my_title = "hello there ...."

    return render(request, "hello_world.html", {"title": my_title})

def about_page(request):
    return render(request, "about.html", {"title": "About us"})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context =   {
        "title": "Contact us",
         "form": form
        }  
    return render(request, "form.html", context)


def example_page(request):
    context          = {"title": "Example"}
    template_name   = "hello_world.html"
    template_obj   = get_template(template_name)
    rendered_item  = template_obj.render(context)
    return HttpResponse(rendered_item)