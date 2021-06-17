from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """
<h1>Mi web personal</h1>
<ul>
     <li><a href="/">Portada</a></li>
     <li><a href="/about/">Acerca de</a></li>
     <li><a href="/portafolio/">portafolio</a></li>
     <li><a href="/contact/">Contacto</a></li>
</ul>
"""


def home(request):
    return render(request, "core/home.html")


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
