from rest_framework import serializers
from alumnos.models import Alumno, Materia, Nota


class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id', 'url', 'nombre', 'insc_date', 'dni')



class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ('id', 'url','nombre')


class NotaSerializer(serializers.HyperlinkedModelSerializer):

    materia = serializers.SerializerMethodField()


    class Meta:
        model = Nota
        fields = ('id', 'url', 'exam_date', 'calificacion', 'alumno_id', 'materia')

    def get_materia(self,obj):
        return obj.materia.nombre
