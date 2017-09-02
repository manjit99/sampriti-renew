from django.shortcuts import render
from django.views import View
from .models import NormalPost

def index(request):
    queryset = NormalPost.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request, "index.html", context)



def about(request):
    return render(request, 'about-us.html',{})

def chief(request):
    return render(request, 'chief.html', {})

def guideline(request):
    return render(request, 'guidelines.html', {})

def advisory(request):
    return render(request, 'advisory.html', {})

def contact(request):
    return render(request, 'contact-us.html', {})

def certificate(request):
    return render(request, 'certificate.html', {})
