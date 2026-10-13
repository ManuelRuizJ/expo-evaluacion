from django.contrib import admin
from .models import Proyecto, Evaluador, Calificacion

class CalificacionesInline(admin.TabularInline):
    model = Calificacion
    extra = 0

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "equipo", "categoria"]
    list_filter = ["categoria"]
    inlines = [CalificacionesInline]

admin.site.register(Evaluador)
admin.site.register(Calificacion)