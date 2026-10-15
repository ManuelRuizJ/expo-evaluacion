from rest_framework import serializers
from .models import Evaluador, Proyecto, Calificacion



class EvaluadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluador
        fields = '__all__'


class EvaluacionDetalleSerializer(serializers.ModelSerializer):
    evaluador = serializers.StringRelatedField()

    class Meta:
        model = Calificacion
        fields = ['evaluador', 'puntaje']


class ProyectoSerializer(serializers.ModelSerializer):
    promedio = serializers.SerializerMethodField()
    evaluaciones = EvaluacionDetalleSerializer(
        source='calificaciones',
        many=True,
        read_only=True
    )

    class Meta:
        model = Proyecto
        fields = [
            'id',
            'titulo',
            'equipo',
            'categoria',
            'promedio',
            'evaluaciones'
        ]

    def get_promedio(self, obj):
        if obj.promedio_puntaje is None:
            return None
        return round(obj.promedio_puntaje, 0)


class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'