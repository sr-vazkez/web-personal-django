from django.shortcuts import render

# Create your views here.


def portafolio(request):
    return render(request, "portafolio/portafolio.html")
