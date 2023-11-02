"""
URL configuration for pig_23654 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from mediturnosApp import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index, name="indice"),
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

