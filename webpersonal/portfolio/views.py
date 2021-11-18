from django.shortcuts import render
# Importar modelos a la app portfolio
from .models import Project

# Create your views here.


def porfolio(request):
    # Crear una lista de proyectos llamada projects
    projects =  Project.objects.all() # Nos devolvera todos los objetos que tiene el modelo de proyecto
    
    # Pasar datos a un template
    return render(request, "portfolio/portfolio.html", {'projects':projects})
