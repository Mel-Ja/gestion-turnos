from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from .forms import SolicitarTurnoForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Medico



# Create your views here.
def solicitarturno(request):
    
    if request.method == "POST":
        #instanciamos un formulario con datos
        formulario = SolicitarTurnoForm(request.POST)

        #validamos
        if formulario.is_valid():
            # dar alta la información

            messages.info(request, "Turno reservado exitosamente")
            return redirect(reverse("indice"))
        
    else: # entro en GET
        formulario= SolicitarTurnoForm()
    
    contexto = {
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M'),
            'formulario': formulario
    }
                
    return render(request, "mediturnosApp/turnos/solicitarturno.html", contexto)


 

def index(request):
    contexto = {
        'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
    return render(request,'mediturnosApp/turnos/indice.html', contexto)

def medicos(request, id_especialidad):
   
    medicos = []

    if id_especialidad == 1:
        medicos = [['Juan Perez','Clinica','1001'],['Laura García','Clinica','1002'],['Ana Martinez','Clinica','1003']]
    elif id_especialidad == 2:
        medicos = [['Carlos López','Pediatria','2001'],['Laura García','Pediatria','2002'],['Diego Fernández','Pediatria','2003']]
    elif id_especialidad == 3:
        medicos = [['María Rodríguez','Traumatologia','3001'],['Pepe Argento','Traumatologia','3002'],['Sofía Torres','Traumatologia','3003']]
    elif id_especialidad == 0:
        medicos = [['Juan Perez','Clinica','1001'],['Laura García','Clinica','1002'],['Ana Martinez','Clinica','1003'],['Carlos López','Pediatria','2001'],['Laura García','Pediatria','2002'],['Diego Fernández','Pediatria','2003'],['María Rodríguez','Traumatologia','3001'],['Pepe Argento','Traumatologia','3002'],['Sofía Torres','Traumatologia','3003']]

    return render(request,'mediturnosApp/turnos/medicos.html',{"id":id_especialidad,"medicos":medicos})

def especialidades(request):
    especialidades = [['Pediatría'], ['Clínica'], ['Traumatología'], ['Cirugía'], ['Obstetricia'], ['Oftalmología'], ]
    contexto = {
            'especialidades': especialidades,
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
                }
    
    return render(request, "mediturnosApp/turnos/especialidades.html", contexto)

def agenda(request):
    contexto = {
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
                }
    return render(request, "mediturnosApp/turnos/agenda.html", contexto)

class MedicoCreateView(CreateView):
    model = Medico
    template_name = 'mediturnosApp/turnos/medicosAlta.html'
    success_url = 'listado'
    fields = '__all__'


# Para que funcione la vista basada en clases, y muestre los medicos que hay en la base de datos
# temporalmente hay que cargar manualmente los medicos, en la base de datos, a traves del pgadmin

class MedicoListView(ListView):
    model = Medico
    context_object_name = 'medicos'
    template_name = 'mediturnosApp/turnos/medicosListado.html' 
    


