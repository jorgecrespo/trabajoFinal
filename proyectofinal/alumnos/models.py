from django.db import models
from django.utils.timezone import now


class Alumno(models.Model):
    nombre = models.CharField(max_length = 255, blank= False, null = False)
    insc_date = models.DateField("Fecha de inscripcion", blank = True, null = True)
    dni = models.CharField(max_length = 255, blank= False, null = False, default = "")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    imagen =  models.ImageField(verbose_name="Imagen", null=True, blank =True,)
    
    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return self.nombre
        

class Materia (models.Model):
    nombre = models.CharField("Nombre", max_length = 255, blank= False, null = False)
    alumnos = models.ManyToManyField(Alumno, through='Nota')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name =  "Materia"
        verbose_name_plural =  "Materias"

    def __str__(self):
        return self.nombre

class Nota ( models.Model):
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
    exam_date = models.DateField(verbose_name="Fecha de examen",blank = False, null = False)
    calificacion = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name =  "Nota"
        verbose_name_plural =  "Notas"

    def __str__(self):
        tostring = str(self.alumno) + ' -> ' +  str(self.materia)  + ' = ' + str(self.calificacion) 
        return  tostring



# Definir max_length de todos los campos



