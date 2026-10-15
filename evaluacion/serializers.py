from rest_framework import serializers
from .models import Evaluador, Proyecto, Calificacion

class EvaluadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluador
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    promedio = serializers.SerializerMethodField()
    class Meta:
        model = Proyecto
        fields = ['id', 'titulo', 'equipo', 'categoria', 'promedio', 'evaluadores']

    def get_promedio(self, obj):
        return round(obj.promedio_puntaje, 0)



class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'