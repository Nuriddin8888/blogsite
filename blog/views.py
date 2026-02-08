from django.shortcuts import render
from .models import Person, About, CaruselBanner
# Create your views here.

def my_profil(request):
    person = Person.objects.all()
    
    context = {
        'persons': person
    }
    
    return render(request, 'base.html', context)


def home_page(request):
    carusel = CaruselBanner.objects.all()
    
    context = {
        'carusels': carusel[:3]
    }
    
    return render(request, 'index.html', context)


def about_page(request):
    about = About.objects.all()
    
    context = {
        'abouts': about
    }
    
    return render(request, 'about.html', context)


def blog_page(request):
    return render(request, 'blog.html')


def contact_page(request):
    return render(request, 'contact.html')


def single_page(request):
    return render(request, 'single.html')