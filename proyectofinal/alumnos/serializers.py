from rest_framework import serializers
from alumnos.models import Alumno, Materia, Nota


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id', 'nombre', 'insc_date', 'dni')



class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ('id','nombre')


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ('id', 'exam_date', 'calificacion', 'alumno', 'materia')
