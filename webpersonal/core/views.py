from django.shortcuts import render, HttpResponse, html_base

# Create your views here.


def home(request):
    return HttpResponse(html_base + """
                         <h2>Inicio</h2>
                         <p>Texto chingon</p>
                         """)


def about(request):
    return HttpResponse(html_base + """
                         <h2>Acerca de Mi</h2>
                         <p>Texto chingon</p>
                         """)


def portafolio(request):
    return HttpResponse(html_base + """
                         <h2>Portafolio</h2>
                         <p>Texto chingon</p>
                         """)


def contact(request):
    return HttpResponse(html_base + """
                         <h2>Contactame</h2>
                         <p>Texto chingon</p>
                         """)
