from django.shortcuts import render, HttpResponse

# Aca se definen las vistas de la app


# Crear una funcion , es una funcion por que forma parte de una clase

def home(request):
    return render(request, "core/home.html")
def about(request):
    return render(request, "core/about.html")
def contact(request):
    return render(request, "core/contact.html")