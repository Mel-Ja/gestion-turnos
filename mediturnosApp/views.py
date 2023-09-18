from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'mediturnosApp/turnos/indice.html')

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
    return render(request, "mediturnosApp/turnos/especialidades.html", {'especialidades':especialidades})

def agenda(request):
      return render(request, "mediturnosApp/turnos/agenda.html")

def solicitarturno(request):
    return render(request, "mediturnosApp/turnos/solicitarturno.html")
