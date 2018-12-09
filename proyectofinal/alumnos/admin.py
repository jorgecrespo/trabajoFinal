from django.contrib import admin
from .models import Alumno, Materia, Nota

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    search_fields = (('nombre','dni'))
    date_hierarchy = 'insc_date'
    list_display = ('dni', 'nombre', 'insc_date', )
    readonly_fields=('created', 'updated')
    


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
    readonly_fields=('created', 'updated')



@admin.register(Nota)
class NotasAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'materia','calificacion', 'exam_date')
    readonly_fields=('created', 'updated')


# admin.site.register(Alumno, AlumnoAdmin)