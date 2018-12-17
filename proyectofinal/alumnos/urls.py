from . import views
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register( 'alumnos', views.AlumnosViewSet )
router.register( 'materias', views.MateriasViewSet )
router. register( 'notas', views.NotasViewSet )

urlpatterns = [
    path( '', include( router.urls)), 
]
