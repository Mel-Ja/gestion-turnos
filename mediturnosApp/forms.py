from django import forms
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError


class SolicitarTurnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Ingrese su nombre'}))
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Ingrese su apellido'}))
    dni = forms.CharField(label="DNI", required=True, widget=forms.TextInput(attrs={'class': 'form-control dni-input', 'pattern': '[0-9]{8}', 'title': 'El DNI debe contener 8 dígitos numéricos', 'maxlength': '8', 'placeholder': 'Ingrese su dni'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su email'}))
    especialidad = forms.CharField(label="Especialidad", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras',}))
    medico = forms.CharField(label="Médico", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', }))
    fecha = forms.DateField(
        label="Fecha",
        required=True,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'min': str(datetime.now().date() + timedelta(days=1))  # Establecemos como fecha mínima el día siguiente al actual
            }
        )
    )
    hora = forms.TimeField(label="Hora", required=True, widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))


    # def clean_especialidad(self):
    #     especialidad = self.cleaned_data.get("especialidad")
    #     especialidad = especialidad.lower() #convertimos a minuscula todo lo que el usuario haya puesto en cada campo
    #     especialidades_permitidas = ["clinica", "pediatria", "traumatologia", "cirugia", "obstetricia", "oftalmologia"]

    #     if especialidad not in especialidades_permitidas:
    #         raise ValidationError("La especialidad ingresada no es válida, las especialidades disponibles son: Clinica, Pediatria, Traumatologia, Cirugia, Obstetricia y Oftalmologia")

    #     return especialidad
    def clean_especialidad(self):
        especialidad = self.cleaned_data["especialidad"]
        especialidades_lista = [['Pediatría'], ['Clínica'], ['Traumatología'], ['Cirugía'], ['Obstetricia'], ['Oftalmología'], ] # Esto lo va a ir a verificar a la BDD

        if especialidad not in [item[0] for item in especialidades_lista]:
            raise forms.ValidationError("Especialidad invalida")
        
        return especialidad

    
    def clean_medico(self):
        medico = self.cleaned_data["medico"]
        especialidad = self.cleaned_data["especialidad"]
        medicos = [['Juan Perez','Clinica','1001'],['Laura García','Clinica','1002'],['Ana Martinez','Clinica','1003'],['María Rodríguez','Traumatología','3001'],['Pepe Argento','Traumatología','3002'],['Sofía Torres','Traumatología','3003'], ['Juan Perez','Clinica','1001'],['Laura García','Clinica','1002'],['Ana Martinez','Clinica','1003'],['Carlos López','Pediatría','2001'],['Laura García','Pediatría','2002'],['Diego Fernández','Pediatría','2003'],['María Rodríguez','Traumatología','3001'],['Pepe Argento','Traumatología','3002'],['Sofía Torres','Traumatología','3003']]

        medicos_especialidad = [medico[0] for medico in medicos if medico[1] == especialidad]
        if medico not in medicos_especialidad:
            raise forms.ValidationError("Médico no válido para esta especialidad")
        
        return medico
        
    def clean_hora(self):
        hora = self.cleaned_data['hora'] 
        horas_ocupadas = [datetime(2023, 10, 4, 10, 0).time(), datetime(2023, 10, 5, 15, 30).time(), datetime(2023, 10, 6, 14, 45).time()]

        if hora in horas_ocupadas:
            raise forms.ValidationError("La hora seleccionada no está disponible")
        
        return hora

    
    
    
    