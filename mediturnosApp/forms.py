from django import forms
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

# Define las opciones de especialidades
ESPECIALIDADES_CHOICES = [
    ('', 'Elegir'),
    ('Pediatría', 'Pediatría'),
    ('Clínica', 'Clínica'),
    ('Traumatología', 'Traumatología'),
    ('Cirugía', 'Cirugía'),
    ('Obstetricia', 'Obstetricia'),
    ('Oftalmología', 'Oftalmología')
]

HOUR_CHOICES = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") for hour in range(8, 20) for minute in range(0, 60, 15)]

class SolicitarTurnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Ingrese su nombre'}))
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Ingrese su apellido'}))
    dni = forms.CharField(label="DNI", required=True, widget=forms.TextInput(attrs={'class': 'form-control dni-input', 'pattern': '[0-9]{8}', 'title': 'El DNI debe contener 8 dígitos numéricos', 'maxlength': '8', 'placeholder': 'Ingrese su dni'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su email'}))
    especialidad = forms.ChoiceField(label="Especialidad", choices=ESPECIALIDADES_CHOICES, widget=forms.Select(attrs={'class': 'form-control solo-letras'}))
    
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
    hora = forms.ChoiceField(
        label="Hora",
        required=True,
        choices=HOUR_CHOICES,  # Utiliza las opciones actualizadas
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    def clean_especialidad(self):
        especialidad = self.cleaned_data.get("especialidad")
        especialidades_lista = ['Pediatría', 'Clínica', 'Traumatología', 'Cirugía', 'Obstetricia', 'Oftalmología'] # Esto lo va a ir a verificar a la BDD

        if especialidad not in especialidades_lista:
            raise ValidationError("La especialidad ingresada no es válida, las especialidades disponibles son: Clínica, Pediatría, Traumatología, Cirugia, Obstetricia y Oftalmologia")
        
        return especialidad

    def clean_medico(self):
        medico = self.cleaned_data.get("medico")
        especialidad = self.cleaned_data.get("especialidad")
        
        medicos = [['Juan Perez','Clínica','1001'],['Laura García','Clínica','1002'],['Ana Martinez','Clínica','1003'],['Carlos López','Pediatría','2001'],['Laura García','Pediatría','2002'],['Diego Fernández','Pediatría','2003'],['María Rodríguez','Traumatología','3001'],['Pepe Argento','Traumatología','3002'],['Sofía Torres','Traumatología','3003']]

        medicos_especialidad = [medico[0] for medico in medicos if medico[1] == especialidad]
        if medico not in medicos_especialidad:
            if especialidad == "Clínica":
                raise forms.ValidationError("Médico no válido para esta especialidad, los medicos disponibles para la especialidad clínica son: Juan Perez, Laura García y Ana Martinez")
            elif especialidad == "Traumatología":
                raise forms.ValidationError("Médico no válido para esta especialidad, los medicos disponibles para la especialidad Traumatología son: María Rodríguez, Pepe Argento y Sofía Torres")
            elif especialidad == "Pediatría":
                raise forms.ValidationError("Médico no válido para esta especialidad, los medicos disponibles para la especialidad Pediatría son: Carlos López, Laura García y Diego Fernández")
        
        return medico
        
    def clean_hora(self):
        hora = self.cleaned_data.get('hora')
        fecha_hora_ocupadas = [
            datetime(2023, 10, 4, 10, 0),
            datetime(2023, 10, 5, 15, 30),
            datetime(2023, 10, 6, 14, 45)
        ]

        for fecha_hora_ocupada in fecha_hora_ocupadas:
            if hora == fecha_hora_ocupada.strftime('%H:%M') and self.cleaned_data['fecha'] == fecha_hora_ocupada.date():
                raise forms.ValidationError("La hora seleccionada no está disponible para esta fecha")

        return hora

    
    
    
    