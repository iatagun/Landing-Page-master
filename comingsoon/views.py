from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from django.http import FileResponse

from django.shortcuts import render
from .models import Shuttle


def home(request):
    context = {}
    template = 'comingsoon/home.html'
    return render(request, template, context)

def team19(request):
    shuttle = Shuttle.objects.all()
    context = {
        'shuttle': shuttle,
    }
    template = 'comingsoon/team19.html'
    return render(request, template, context)

def team20(request):
    shuttle = Shuttle.objects.all()
    context = {
        'shuttle': shuttle,
    }
    template = 'comingsoon/team20.html'
    return render(request, template, context)

def team21(request):
    shuttle = Shuttle.objects.all()
    context = {
        'shuttle': shuttle,
    }
    template = 'comingsoon/team21.html'
    return render(request, template, context)