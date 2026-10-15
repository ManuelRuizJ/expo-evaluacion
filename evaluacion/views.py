# evaluacion/views.py
from django.db.models import Avg, Count
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Evaluador, Proyecto, Calificacion
from .serializers import EvaluadorSerializer, ProyectoSerializer, CalificacionSerializer

class EvaluadorViewSet(viewsets.ModelViewSet):
    queryset = Evaluador.objects.all()
    serializer_class = EvaluadorSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer

    def get_queryset(self):
        return Proyecto.objects.annotate(
            promedio_puntaje=Avg('calificaciones__puntaje')
        )

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class StatsViewSet(viewsets.ReadOnlyModelViewSet):
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

class StatsDashboardView(APIView):
    def get(self, request):
        promedio_general = Calificacion.objects.aggregate(
            promedio=Avg('puntaje')
        )['promedio']

        proyectos_por_categoria = Proyecto.objects.values(
            'categoria'
        ).annotate(
            total=Count('id')
        ).order_by('categoria')

        mejores_proyectos = Proyecto.objects.annotate(
            promedio_puntaje=Avg('calificaciones__puntaje')
        ).exclude(
            promedio_puntaje__isnull=True
        ).order_by('-promedio_puntaje')[:5]

        return Response({
            'resumen': {
                'total_proyectos': Proyecto.objects.count(),
                'total_evaluadores': Evaluador.objects.count(),
                'total_calificaciones': Calificacion.objects.count(),
                'promedio_general': (
                    round(promedio_general, 2)
                    if promedio_general is not None
                    else None
                ),
            },
            'proyectos_por_categoria': list(proyectos_por_categoria),
            'mejores_proyectos': ProyectoSerializer(
                mejores_proyectos,
                many=True
            ).data,
        })