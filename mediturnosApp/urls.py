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
    path('medicos/', views.medicos, name="medicos"),
    path('medicos/<int:id_especialidad>/', views.medicosxesp, name="medicosxesp"),
    path('agenda/', views.agenda, name="agenda"),
    path('medicos/alta', views.MedicoCreateView.as_view(), name="medicos-alta"),
    path('medicos/listado', views.MedicoListView.as_view(), name="medicos-listado"),
    path('especialidades/alta', views.EspecialidadCreateView.as_view(), name="especialidad-alta"),
    path('pacientes/alta', views.PacienteCreateView.as_view(), name="pacientes-alta"),
    path('pacientes/turnos', views.TurnosCreateView.as_view(), name="solicitar-turno"),
    path('verificar_dni', views.verificar_dni, name='verificar_dni'),
    
 
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)