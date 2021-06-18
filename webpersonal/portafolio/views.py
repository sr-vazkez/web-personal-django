from django.shortcuts import render
from .models import Project

# Create your views here.


def portafolio(request):
    projects = Project.objects.all().order_by('-created')
    return render(request, "portafolio/portafolio.html", {'projects': projects})
