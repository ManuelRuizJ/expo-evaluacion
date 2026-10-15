from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EvaluadorViewSet, ProyectoViewSet, CalificacionViewSet, StatsViewSet

router = DefaultRouter()
router.register(r'evaluadores', EvaluadorViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'calificaciones', CalificacionViewSet)
router.register(r'stats/proyectos/calificaciones', StatsViewSet, basename='stats-proyectos') 

urlpatterns = [
    path('api/', include(router.urls)),
]