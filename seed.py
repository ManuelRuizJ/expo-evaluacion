import os
import django
import random

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # Ajusta 'config' si tu carpeta de settings se llama distinto
django.setup()

from evaluacion.models import Evaluador, Proyecto, Calificacion

def poblar_datos():
    print("🧹 Limpiando base de datos existente...")
    Calificacion.objects.all().delete()
    Evaluador.objects.all().delete()
    Proyecto.objects.all().delete()

    print("🚀 Creando lista ampliada de evaluadores...")
    nombres_evaluadores = [
        "Ana Pérez", "Carlos Gómez", "María Rodríguez", "Jorge Martínez", 
        "Lucía Fernández", "David López", "Sofía Sánchez", "Mateo Ramírez",
        "Valentina Torres", "Alejandro Díaz", "Camila Ruiz", "Andrés Morales"
    ]
    
    evaluadores = []
    for i, nombre in enumerate(nombres_evaluadores):
        # Generar un correo único y limpio basado en el nombre
        correo_base = nombre.lower().replace(" ", ".")
        evaluador = Evaluador.objects.create(
            nombre=nombre,
            correo=f"{correo_base}{i+1}@universidad.edu"
        )
        evaluadores.append(evaluador)

    print("🚀 Creando lista ampliada de proyectos...")
    datos_proyectos = [
        # Hardware
        ("Sistema de Gestión IoT Industrial", "Equipo Alpha", Proyecto.Categoria.HARDWARE),
        ("Robot Autónomo de Limpieza", "RoboTech", Proyecto.Categoria.HARDWARE),
        ("Casco Inteligente para Ciclistas", "SafeRide", Proyecto.Categoria.HARDWARE),
        ("Brazo Robótico Controlado por Gestos", "CyberMec", Proyecto.Categoria.HARDWARE),
        
        # Inteligencia Artificial
        ("Asistente IA para Diagnóstico Médico", "NeuralDevs", Proyecto.Categoria.IA),
        ("Detección de Fraude Bancario con ML", "DataMinds", Proyecto.Categoria.IA),
        ("Traductor Automático de Lengua de Señas", "SignAI", Proyecto.Categoria.IA),
        ("Generador de Resúmenes Académicos", "TextMind", Proyecto.Categoria.IA),
        
        # Software
        ("Plataforma Cloud de E-commerce", "ShopifyPros", Proyecto.Categoria.SOFTWARE),
        ("Sistema de Control de Inventarios ERP", "LogiSoft", Proyecto.Categoria.SOFTWARE),
        ("Gestor de Tareas Ágiles tipo Trello", "TaskFlow", Proyecto.Categoria.SOFTWARE),
        ("Banco Digital de Microcréditos", "FinTech Solutions", Proyecto.Categoria.SOFTWARE),
        ("Red Social Académica e Investigativa", "EduConnect", Proyecto.Categoria.SOFTWARE),
        ("API Gateway de Alto Rendimiento", "FastCore", Proyecto.Categoria.SOFTWARE),
        
        # Social
        ("App de Apoyo Comunitario y Donaciones", "SocialCode", Proyecto.Categoria.SOCIAL),
        ("Sistema de Riego Automatizado para Comunidades", "AgroSmart", Proyecto.Categoria.SOCIAL),
        ("Plataforma de Mentorías para Jóvenes", "FuturoJOV", Proyecto.Categoria.SOCIAL),
        ("Mapa Interactivo de Alertas Ciudadanas", "SafeCity", Proyecto.Categoria.SOCIAL),
        ("Red de Economía Circular Local", "EcoBarrio", Proyecto.Categoria.SOCIAL),
        ("App de Salud Mental y Apoyo Psicológico", "MindCare", Proyecto.Categoria.SOCIAL),
    ]

    proyectos = []
    for titulo, equipo, categoria in datos_proyectos:
        proyecto = Proyecto.objects.create(
            titulo=titulo,
            equipo=equipo,
            categoria=categoria
        )
        proyectos.append(proyecto)

    print("🚀 Generando calificaciones y comentarios variados...")
    comentarios_ejemplo = [
        "Excelente presentación, defensa y dominio técnico impecable.",
        "Muy buena idea, aunque la interfaz de usuario requiere un par de ajustes.",
        "Proyecto altamente innovador con un gran impacto social real.",
        "La arquitectura del sistema es sólida, escalable y muy limpia.",
        "Podría mejorar la documentación técnica y las pruebas unitarias.",
        "El modelo de negocio planteado es muy viable y realista.",
        "Sorprendente nivel de ejecución para el tiempo disponible.",
        "Le faltó profundizar un poco más en los casos de borde o fallos.",
        "Una propuesta fresca y muy bien desarrollada. ¡Muchas felicidades!"
    ]

    contador = 0
    for proyecto in proyectos:
        # Asignamos de forma completamente aleatoria entre 4 y 8 evaluadores por proyecto
        evaluadores_asignados = random.sample(evaluadores, k=random.randint(4, 8))
        
        for evaluador in evaluadores_asignados:
            # Puntaje decimal realista entre 4.00 y 10.00
            puntaje_aleatorio = round(random.uniform(4.0, 10.0), 2)
            comentario = random.choice(comentarios_ejemplo)

            # Evitar duplicados respetando la restricción única del modelo
            if not Calificacion.objects.filter(evaluador=evaluador, proyecto=proyecto).exists():
                Calificacion.objects.create(
                    proyecto=proyecto,
                    evaluador=evaluador,
                    puntaje=puntaje_aleatorio,
                    comentario=comentario
                )
                contador += 1

    print(f"¡Éxito total! Se crearon {len(evaluadores)} evaluadores, {len(proyectos)} proyectos únicos y {contador} calificaciones variadas.")

if __name__ == '__main__':
    poblar_datos()