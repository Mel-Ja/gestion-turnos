from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from .forms import SolicitarTurnoForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Medico, Especialidad, Paciente, Turnos
from .forms import MedicoAltaForm, PacienteAltaForm, TurnosAltaForm
from django.http import JsonResponse



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
    return render(request,'mediturnosApp/index/indice.html', contexto)

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

    return render(request,'mediturnosApp/medicos/medicos.html',{"id":id_especialidad,"medicos":medicos})

def especialidades(request):
    especialidades = [['Pediatría'], ['Clínica'], ['Traumatología'], ['Cirugía'], ['Obstetricia'], ['Oftalmología'], ]
    contexto = {
            'especialidades': especialidades,
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
                }
    
    return render(request, "mediturnosApp/especialidades/especialidades.html", contexto)

def agenda(request):
    contexto = {
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
                }
    return render(request, "mediturnosApp/turnos/agenda.html", contexto)

# class MedicoCreateView(CreateView):
#     model = Medico
#     template_name = 'mediturnosApp/turnos/medicos-alta.html'
#     success_url = '/'
#     fields = '__all__'
    
class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoAltaForm  # Usa el formulario personalizado del modelForms de forms.py
    template_name = 'mediturnosApp/medicos/medicos-alta.html'
    success_url = '/'

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Aclaracion importe!!
# Para probarlo y que funcione, temporalmente, primero se debe cargar las especialidades en 
# el frontend, en la seccion "Alta de especialidad"
# y luego si, cargar el alta de un medico en la seccion "Alta de medico"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class MedicoListView(ListView):
    model = Medico
    context_object_name = 'medicos'
    template_name = 'mediturnosApp/medicos/medicos-nuevos-listado.html' 
    
class EspecialidadCreateView(CreateView):
    model = Especialidad
    template_name = 'mediturnosApp/especialidades/especialidades-alta.html'
    success_url = '/'
    fields = '__all__'
    
    
class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteAltaForm  # Usa el formulario personalizado del modelForms de forms.py
    template_name = 'mediturnosApp/pacientes/pacientes-alta.html'
    success_url = '/'    


class TurnosCreateView(CreateView):
    model = Turnos
    form_class = TurnosAltaForm  # Usa el formulario personalizado del modelForms de forms.py
    template_name = 'mediturnosApp/turnos/solicitarturno.html'
    success_url = '/'    

################### No borrar, es una alternativa para chequear si un dni existe ##############
def verificar_dni(request): #Definimos una función de vista llamada verificar_dni, que atendera cuando se ingrese en el navegador "/verificar_dni", o cuando se envien datos a esa direccion. Esta funcion de vista, a la que le llegan datos en el request, verificara si el dni del paciente existe. 
    if request.method == "POST": #Si el metodo es POST, significa que el usuario apreto enviar al formulario, y nos mando el dni
        dni = request.POST.get("dni") #Obtenemos el valor del campo dni, de los datos que se enviaron en la request por el usuario
        existe_paciente = Paciente.objects.filter(dni=dni).exists() # buscamos si existe algún registro en la base de datos de la tabla Paciente que tenga ese numero de dni. El resultado es un valor booleano que indica si existe un paciente con ese DNI. Este valor se almacena en la variable existe_paciente
        datosDeRespuesta = { #Creamos un diccionario llamado datosDeRespuesta con una clave "existe" que contiene el valor de existe_paciente. Este diccionario se utilizará para construir la respuesta JSON.
            'existe': existe_paciente
        }
        return JsonResponse(datosDeRespuesta) # Respondemos a la solicitud enviando una respuesta JSON al cliente frontend. Mandando el diccionario 
    
    else: #Si la solicitud no es de tipo POST, se responde con un JSON que contiene la clave "existe" establecida en False. 
       return JsonResponse({'existe': False})
################### No borrar, es una alternativa para chequear si un dni existe ##############   
   
   
   
######################### No borrar, me da una idea de algo a futuro ##############################   
# def crear_turno(request):
#     if request.method == 'POST':
#         form = TurnosAltaForm(request.POST)
#         if form.is_valid():
#             # Aquí debes asegurarte de establecer la fecha antes de guardar el objeto
#             turno = form.save(commit=False)
#             turno.fecha = form.cleaned_data['fecha']
#             turno.save()
#             return redirect('ruta_de_redireccion')  # Redirige a la página deseada después de guardar el turno
#     else:
#         form = TurnosAltaForm()
#     return render(request, 'template.html', {'form': form})
######################### No borrar, me da una idea de algo a futuro ##############################   