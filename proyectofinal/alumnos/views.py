from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from alumnos.models import Alumno, Materia
from alumnos.serializers import AlumnoSerializer, MateriaSerializer


@csrf_exempt
def alumnos_list(request):
    alumnos = Alumno.objects.all()
    serializer = AlumnoSerializer(alumnos, many = True)
    return JsonResponse(serializer.data, safe = False)


@csrf_exempt
def materias_list(request):
    materias = Materia.objects.all()
    serializer = MateriaSerializer(materias, many = True)
    return JsonResponse(serializer.data, safe = False)


@csrf_exempt
def notas_list(request):
    notas = Materia.objects.all()
    serializer = MateriaSerializer(notas, many = True)
    return JsonResponse(serializer.data, safe = False)