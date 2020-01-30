from django.contrib import admin
from .models import equipo, runners,carreras,individual,carrera_activa

# Register your models here.

admin.site.register(equipo)
admin.site.register(runners)
admin.site.register(carreras)
admin.site.register(individual)
admin.site.register(carrera_activa)