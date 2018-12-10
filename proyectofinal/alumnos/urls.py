from django.urls import path

from . import views

urlpatterns = [
    path('alumnos/', views.alumnos_list),
    path('materias/', views.materias_list),
    path('notas/<int:alumno>/', views.notas_list)
]

#XXXXXXXXXXX
