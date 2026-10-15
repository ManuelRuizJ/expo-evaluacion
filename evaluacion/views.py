# evaluacion/views.py
from django.db.models import Avg
from rest_framework import viewsets
from .models import Evaluador, Proyecto, Calificacion
from .serializers import EvaluadorSerializer, ProyectoSerializer, CalificacionSerializer

class EvaluadorViewSet(viewsets.ModelViewSet):
    queryset = Evaluador.objects.all()
    serializer_class = EvaluadorSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class StatsViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    def get_queryset(self):
        queryset = Proyecto.objects.annotate(
            promedio_puntaje=Avg('calificaciones__puntaje')
        ).order_by('-promedio_puntaje')

        categoria = self.request.query_params.get('categoria')
        
        if categoria:
            queryset = queryset.filter(categoria__iexact=categoria)

        return queryset
