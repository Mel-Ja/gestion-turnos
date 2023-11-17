from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import SolicitarTurnoForm
from .forms import EspecialidadForm, MedicoAltaForm, PacienteAltaForm, TurnosAltaForm
from .models import Especialidad, Medico, Paciente, Turnos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
def index(request):
    contexto = {
        'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
    
    return render(request,'mediturnosApp/index/indice.html', contexto)

def inicioDeSesion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("indice")
        else:
            messages.error(request, "Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
    
    # Asegúrate de devolver una respuesta HTTP incluso si las credenciales son incorrectas
    return render(request, 'mediturnosApp/index/login.html')
 
 
def cerrarSesion(request):
    logout(request)
    return redirect("indice") 
 
def especialidades(request):
    listado = Especialidad.objects.all().order_by('nombre')
    context = {
        'especialidades': listado,
        # 'cant_especialidades': len(listado),
    }

    return render(request, 'mediturnosApp/especialidades/especialidades.html', context)


def medicos(request):
    listado = Medico.objects.all().order_by('apellido')
    context = {
        'medicos' : listado,
    }

    return render(request, 'mediturnosApp/medicos/medicos.html', context)

def medicosxesp(request, id_especialidad):
    medicos = []

    if id_especialidad == 1:
        medicos = [['Juan Perez','Clinica','1001'],['Laura García','Clinica','1002'],['Ana Martinez','Clinica','1003']]
    elif id_especialidad == 2:
        medicos = [['Carlos López','Pediatria','2001'],['Laura García','Pediatria','2002'],['Diego Fernández','Pediatria','2003']]
    elif id_especialidad == 3:
        medicos = [['María Rodríguez','Traumatologia','3001'],['Pepe Argento','Traumatologia','3002'],['Sofía Torres','Traumatologia','3003']]
    elif id_especialidad == 0:
        medicos = [['Juan Perez','Clinica','1001'],['Laura García','Clinica','1002'],['Ana Martinez','Clinica','1003'],['Carlos López','Pediatria','2001'],['Laura García','Pediatria','2002'],['Diego Fernández','Pediatria','2003'],['María Rodríguez','Traumatologia','3001'],['Pepe Argento','Traumatologia','3002'],['Sofía Torres','Traumatologia','3003']]

    return render(request,'mediturnosApp/medicos/medicos-especialidad.html',{"id":id_especialidad,"medicos":medicos})
    # listado = Medico.objects.all().order_by('apellido')
    # context = {
    #     'nombre': listado.nombre,
    #     'apellido': listado.apellido,
    #     'email': listado.email,
    #     'matricula': listado.matricula,
    # }

    # return render(request, 'mediturnosApp/medicos/medicos.html', context)


@login_required
def solicitarturno(request):
    
    if request.method == "POST":
        #instanciamos un formulario con datos
        formulario = SolicitarTurnoForm(request.POST)

        #validamos
        if formulario.is_valid():
            # dar alta la información

            messages.success(request, "Turno reservado exitosamente")
            return redirect(reverse("indice"))
        
    else: # entro en GET
        formulario= SolicitarTurnoForm()
    
    contexto = {
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M'),
            'formulario': formulario
    }
                
    return render(request, "mediturnosApp/turnos/solicitarturno.html", contexto)


def agenda(request):
    contexto = {
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
                }
    return render(request, "mediturnosApp/turnos/agenda.html", contexto)
    


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Aclaracion importe!!
# Para probarlo y que funcione, temporalmente, primero se debe cargar las especialidades en 
# el frontend, en la seccion "Alta de especialidad"
# y luego si, cargar el alta de un medico en la seccion "Alta de medico"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class MedicoListView(ListView):
    model = Medico
    context_object_name = 'medicos'
    template_name = 'mediturnosApp/medicos/medicos.html' 
    
class MedicoPorEspecialidadListView(ListView):
    model = Medico
    context_object_name = 'medicos'
    template_name = 'mediturnosApp/medicos/medicos-por-especialidad.html'

    def get_queryset(self):
        especialidad_id = int(self.kwargs['especialidad_id'])
        return Medico.objects.filter(medicoespecialidad__especialidad__id=especialidad_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        especialidad_id = int(self.kwargs['especialidad_id'])
        try:
            especialidad = Especialidad.objects.get(id=especialidad_id)
            especialidad_nombre = especialidad.nombre
        except Especialidad.DoesNotExist:
            especialidad_nombre = None

        context['especialidad_id'] = especialidad_id
        context['especialidad_nombre'] = especialidad_nombre
        return context
    
    

class MedicoCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('mediturnosApp.add_medico')
    model = Medico
    form_class = MedicoAltaForm  # Usamos el formulario personalizado del modelForms de forms.py
    template_name = 'mediturnosApp/medicos/medicos-alta.html'
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el conteo de especialidades y agregarlo al contexto
        context['cantidad_especialidades'] = Especialidad.objects.count()
        return context
    
    def handle_no_permission(self):
        # Personaliza la redirección cuando el usuario no tiene el permiso
        return redirect('login')

class EspecialidadCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('mediturnosApp.add_especialidad')
    model = Especialidad
    template_name = 'mediturnosApp/especialidades/especialidades-alta.html'
    success_url = '/'
    fields = '__all__'

    def handle_no_permission(self):
        # Personaliza la redirección cuando el usuario no tiene el permiso
        return redirect('login')
    
class PacienteCreateView(PermissionRequiredMixin,CreateView):
    permission_required = ('mediturnosApp.add_paciente')
    model = Paciente
    form_class = PacienteAltaForm  # Usamos el formulario personalizado del modelForms de forms.py
    template_name = 'mediturnosApp/pacientes/pacientes-alta.html'
    success_url = '/'

    def handle_no_permission(self):
        # Personaliza la redirección cuando el usuario no tiene el permiso
        return redirect('login')

class TurnosCreateView(LoginRequiredMixin, CreateView):
    model = Turnos
    form_class = TurnosAltaForm  # Usamos el formulario personalizado del modelForms de forms.py
    template_name = 'mediturnosApp/turnos/solicitarturno.html'
    success_url = '/'    

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Turno reservado exitosamente")
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el conteo de especialidades y agregarlo al contexto
        context['cantidad_medicos'] = Medico.objects.count()
        context['cantidad_pacientes'] = Paciente.objects.count()
        return context    
    
    
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



# Vista utilizada para traer los medicos que correspondan a la especialidad que el usuario elige en el front.
# Esta vista retorna un JSON y lo procesamos desde app.js para retornar los medicos correspondientes en el Select correspondiente.

def cargar_medicos(request):
    especialidad_id = request.GET.get('especialidad_id') #pone el id de la especialidad elegida por el usuario, que llega en el request, en la variable especialidad_id
    # La consulta de abajo lo que hace es acceder a los campos de la relación entre medico y especialidad.
    medicos = Medico.objects.filter(medicoespecialidad__especialidad__id=especialidad_id) #trae de la tabla medicos, a todos los medicos, que tengan en la tabla relacionada MedicoEspecialidad, el id de la especialidad elegida por el usuario. Los guiones bajos se utilizan para navegar a través de las relaciones en el modelo. En este caso, parece que hay una relación entre Medico y Especialidad llamada medicoespecialidad
    medicos_list = [{"id": medico.matricula, "nombre": medico.nombre_completo()} for medico in medicos] #crea un diccionario en la variable medicos_list, donde recorre con un for la lista medicos, y en cada iteracion hace un clave - valor
    return JsonResponse(medicos_list, safe=False)
    #safe=False permite la serialización de tipos de datos que no son básicos de Python. En este caso, se permite la serialización de listas (y no solo de diccionarios). Esto es útil cuando se quiere serializar una lista de objetos, como en este caso, donde medicos_list es una lista de diccionarios.
    #safe=False se utiliza en este caso porque estamos serializando una lista (medicos_list) en lugar de un objeto JSON único. Esto le indica a Django que no debe asumir automáticamente que el objeto a serializar es seguro y le permite serializar listas.