from django.contrib import admin
from mediturnosApp.models import Medico, Paciente, Especialidad, MedicoEspecialidad, Turnos


admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Especialidad)
admin.site.register(MedicoEspecialidad)
admin.site.register(Turnos)
