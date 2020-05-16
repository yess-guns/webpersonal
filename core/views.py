from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about-me/">Acerca de</a></li>
        <li><a href="/porfolio">Portafolio</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")
        
def porfolio(request):
    return render(request, "core/porfolio.html")
       
  
def contact(request):
    return render(request, "core/contact.html")
        
  