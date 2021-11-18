from django.contrib import admin
from .models import Project

# Register your models here.

#  Crear una clase para mostrar el campo 'created' y 'update'
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')
 
admin.site.register(Project, ProjectAdmin)
