from django.db import models

# Create your models here.

# Crear modelos

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(max_length=400, verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects") 
    #   upload_to : guardar todas las img dentro de projects, para que no haya confusion cuando se creen varios modelos con imagenes
    link = models.URLField(null=True, blank=True, verbose_name="Direccion web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion") 
    # Se agregara automaticamente la fecha luego de ser creada, pero solo una vez 
    update = models.DateTimeField(auto_now=True, verbose_name="Ultima modificacion") 
    #  Se ejecuta cada vez que se actualiza
    
    # La clase Meta sirve para añadir metadatos y en este caso la ocuparemos para traducir el nombre de nuestro Modelo
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"] 
        #  Se pone un guion para que muestre los datos mas antiguos
        
    def __str__(self):
        return self.title
    
    
    
