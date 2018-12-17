
from django.shortcuts import render
from rest_framework import viewsets, filters

from alumnos.models import Alumno, Materia, Nota
from alumnos.serializers import AlumnoSerializer, MateriaSerializer, NotaSerializer

from django_filters.rest_framework import DjangoFilterBackend

class AlumnosViewSet( viewsets.ModelViewSet ):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer



class MateriasViewSet( viewsets.ModelViewSet ):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class NotasViewSet( viewsets.ModelViewSet ):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    #defino filtro de alumno, para ver notas de un alumno
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('alumno',)


