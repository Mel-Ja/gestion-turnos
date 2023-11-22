from django.urls import path, re_path
from . import views
from mediturnosApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name="indice"),
    path('login/', views.inicioDeSesion, name="login"),
    path('cerrar-sesion/', views.cerrarSesion, name="cerrar-sesion"),
    path('especialidades/', views.especialidades, name="especialidades"),
    path('medicos/<int:id_especialidad>/', views.medicosxesp, name="medicosxesp"),
    path('agenda/', views.agenda, name="agenda"),
    path('medicos/alta', views.MedicoCreateView.as_view(), name="medicos-alta"),
    path('medicos/listado', views.MedicoListView.as_view(), name="medicos-listado"),
    path('medicos-listado-por-especialidad/<int:especialidad_id>/', views.MedicoPorEspecialidadListView.as_view(), name='medicos-listado-por-especialidad'),
    path('especialidades/alta', views.EspecialidadCreateView.as_view(), name="especialidad-alta"),
    path('pacientes/alta/', views.PacienteCreateView.as_view(), name="pacientes-alta"),
    path('pacientes/turnos', views.TurnosCreateView.as_view(), name="solicitar-turno"),
    path('verificar_dni', views.verificar_dni, name='verificar_dni'),
    path('cargar_medicos/', views.cargar_medicos, name='cargar_medicos'),

    path('administracion/', views.administracion_index, name="administracion_index"),
    path('administracion/especialidades', views.EspecialidadesAdminListView.as_view(), name="especialidades_index"),
    path('administracion/especialidades/alta', views.especialidades_alta, name="especialidades_alta"),
    path('administracion/especialidades/eliminar', views.especialidades_eliminar, name="especialidades_eliminar"),
    path('administracion/especialidades/modificar', views.especialidades_modificar, name="especialidades_modificar"),

    path('administracion/medicos', views.MedicoAdminListView.as_view(), name="medicos_index"),
    path('administracion/medicos/alta', views.MedicoAdminCreateView.as_view(), name="medicos_alta"),
    path('administracion/medicos/eliminar/<int:pk>', views. MedicoAdminDeleteView.as_view(), name="medicos_eliminar"),
    path('administracion/medicos/modificar/<int:pk>', views.MedicoAdminUpdateView.as_view(), name="medicos_modificar"),

    path('administracion/pacientes', views.PacienteListView.as_view(), name="pacientes_index"),
    path('administracion/pacientes/alta', views.PacienteAdminCreateView.as_view(), name="pacientes_alta"),
    path('administracion/pacientes/eliminar/<int:pk>', views.PacienteDeleteView.as_view(), name="pacientes_eliminar"),
    path('administracion/pacientes/modificar/<int:pk>', views.PacienteUpdateView.as_view(), name="pacientes_modificar"),

    path('administracion/turnos', views.TurnosAdminListView.as_view(), name="turnos_index"),
    path('administracion/turnos/cancelar', views.turnos_cancelar, name="turnos_cancelar"),

    path('administracion/perfil', views.perfil_index, name="perfil_index"),
    path('administracion/perfil', views.recuperar_password, name="recuperar_password"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)