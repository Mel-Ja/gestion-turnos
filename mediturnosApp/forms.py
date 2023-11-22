from django import forms
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from .models import Especialidad, Medico, Paciente, Turnos
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

HOUR_CHOICES = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") for hour in range(8, 20) for minute in range(0, 60, 15)]

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion', 'imagen']

class SolicitarTurnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Ingrese su nombre'}))
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Ingrese su apellido'}))
    dni = forms.CharField(label="DNI", required=True, widget=forms.TextInput(attrs={'class': 'form-control dni-input', 'pattern': '[0-9]{8}', 'title': 'El DNI debe contener 8 dígitos numéricos', 'maxlength': '8', 'placeholder': 'Ingrese su dni'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su email'}))
    # especialidad = forms.ChoiceField(label="Especialidad", choices=ESPECIALIDADES_CHOICES, widget=forms.Select(attrs={'class': 'form-control solo-letras'}))
    
    # medico = forms.ChoiceField(label="Médico", choices=MEDICOS_CHOICES, widget=forms.Select(attrs={'class': 'form-control solo-letras', }))
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
            datetime(2023, 10, 6, 10, 0),
            datetime(2023, 10, 9, 15, 30),
            datetime(2023, 10, 10, 14, 45)
        ]

        for fecha_hora_ocupada in fecha_hora_ocupadas:
            if hora == fecha_hora_ocupada.strftime('%H:%M') and self.cleaned_data['fecha'] == fecha_hora_ocupada.date():
                raise forms.ValidationError("La hora seleccionada no está disponible para esta fecha")

        return hora

class MedicoAltaForm(forms.ModelForm):
    # Definimos los campos adicionales de Persona, que no se muestran en el formulario 
    # si no los ponemos manualmente
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    email = forms.EmailField(label="Email", required=True)
    dni = forms.IntegerField(label="DNI", required=True)

    def clean_matricula(self):
        if int(self.cleaned_data['matricula']) < 0:
            raise ValidationError("La matrícula debe ser un número positivo")
        
        return self.cleaned_data['matricula']

    def clean_dni(self):
        if not (0 < self.cleaned_data['dni'] <= 99999999):
            raise ValidationError("El dni debe ser un número positivo")
        
        if len(str(self.cleaned_data['dni'])) < 8:
            raise ValidationError("El dni debe contener al menos 8 caracteres")

        return self.cleaned_data['dni']

    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'email', 'dni', 'matricula', 'especialidades']
        widgets = {
            'especialidades': forms.CheckboxSelectMultiple(),
        }

class PacienteAltaForm(forms.ModelForm):

    username = forms.CharField(max_length=30, label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    def clean_historia_clinica(self):
        if int(self.cleaned_data['historia_clinica']) < 0:
            raise ValidationError("La historia clínica debe ser un número positivo")
        return self.cleaned_data['historia_clinica']


    def clean_dni(self):
        if not (0 < self.cleaned_data['dni'] <= 99999999):
            raise ValidationError("El dni debe ser un número positivo")
        
        if len(str(self.cleaned_data['dni'])) < 8:
            raise ValidationError("El dni debe contener al menos 8 caracteres")

        return self.cleaned_data['dni']
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso")
        return username

    def save(self, commit=True):
        paciente = super(PacienteAltaForm, self).save(commit=False)
        user = User(username=self.cleaned_data['username'])
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
            paciente.user = user  # Asigna el usuario al paciente
            paciente.save()
            self.save_m2m()

        # Asigna el permiso al usuario
            grupo_paciente, creado = Group.objects.get_or_create(name='Paciente')  # Crea o obtiene el grupo 'Paciente'
            paciente.user.groups.add(grupo_paciente)  # Asigna el usuario al grupo 'Paciente'

            
        return paciente

    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'email', 'dni', 'historia_clinica', 'username', 'password']
        labels = {
            'historia_clinica': 'Alta única de historia clínica',
        }
        
        
HOUR_CHOICES = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") for hour in range(8, 20) for minute in range(0, 60, 15)]

class TurnosAltaForm(forms.ModelForm):
    especialidad = forms.ModelChoiceField(
        label="Especialidad",
        queryset=Especialidad.objects.all(),  # Obtener todas las especialidades de la base de datos
        empty_label="Seleccione una especialidad",  # Opcional: Puedes agregar un label inicial
        widget=forms.Select(attrs={'class': 'form-control', 'id':'id_especialidad', 'onchange':'cargarMedicos()'})
    )

    matricula = forms.ModelChoiceField(
        label="Médicos",
        queryset=Medico.objects.all(),
        empty_label="Seleccione un médico",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_medico'})
    )

    fecha = forms.DateField(
        label="Fecha",
        required=True,  # Hacer que la fecha sea obligatoria
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'min': str(datetime.now().date() + timedelta(days=1))
            }
        )
    )
    hora = forms.ChoiceField(
        label="Hora",
        required=True,
        choices=HOUR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Hacemos que el campo "cancelado", no se muestre al usuario en el frontend, y lo seteamos con valor predeterminado False
    # Esto es porque la base de datos tiene como obligatorio enviar este campo
    # Tambien agregamos el campo required=false para que no nos muestre error en el frontend
    # Pero el campo cancelado = false se envia a la base de datos
    cancelado = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput())
    
    def __init__(self, *args, **kwargs):
        super(TurnosAltaForm, self).__init__(*args, **kwargs)
        # Personaliza la representación del campo historia_clinica
        self.fields['historia_clinica'].label_from_instance = lambda obj: f"{obj.nombre} {obj.apellido}"


    class Meta:
        model = Turnos
        fields = ['historia_clinica', 'especialidad', 'matricula', 'fecha', 'hora', 'cancelado']  # Agregar 'fecha' y 'hora' al formulario
        labels = {
            'historia_clinica': 'Paciente',
        }