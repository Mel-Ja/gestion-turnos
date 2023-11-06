from django.contrib import admin
from mediturnosApp.models import Medico, Paciente, Especialidad, MedicoEspecialidad, Turnos


class MedicoEspecialidadInline(admin.TabularInline):
    model = MedicoEspecialidad


class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    inlines = [
       MedicoEspecialidadInline,
    ]

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('historia_clinica', 'nombre', 'apellido')
    list_editable = ('nombre', 'apellido')
    list_display_links = ['historia_clinica']
    search_fields = ['apellido', 'nombre']


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('matricula','apellido', 'nombre')
    search_fields = ['apellido', 'nombre', 'matricula']
    inlines = [
       MedicoEspecialidadInline,
    ]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'especialidades':
            kwargs["queryset"] = Especialidad.objects.filter(nombre__startswith="").order_by("nombre")
        
        return super().formfield_for_manytomany(db_field, request, **kwargs)



admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Turnos)
