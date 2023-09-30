from django import forms	
from datetime import date
	
class SolicitarTurnoForm(forms.Form):	
	
	nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'pattern': '[a-zA-ZáéíóúÁÉÍÓÚ\s]+', 'title': 'Ingrese solo letras', 'class': 'solo-letras'}))
	apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={'pattern': '[a-zA-ZáéíóúÁÉÍÓÚ\s]+', 'title': 'Ingrese solo letras', 'class': 'solo-letras'}))
	dni = forms.CharField(label="Dni", required=True, widget=forms.TextInput(attrs={'pattern': '[0-9]{8}', 'title': 'El DNI debe contener 8 dígitos numéricos', 'class': 'dni-input', 'maxlength': '8'}))
	email = forms.EmailField(label="Email", required=True)
	especialidad = forms.CharField(label="Especialidad", required=True, widget=forms.TextInput(attrs={'pattern': '[a-zA-ZáéíóúÁÉÍÓÚ\s]+', 'title': 'Ingrese solo letras', 'class': 'solo-letras'}))
	medico = forms.CharField(label="Medico", required=True, widget=forms.TextInput(attrs={'pattern': '[a-zA-ZáéíóúÁÉÍÓÚ\s]+', 'title': 'Ingrese solo letras', 'class': 'solo-letras'}))
	fecha = forms.DateField(
        label="Fecha",
        required=True,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'min': str(date.today())  # Establecemos como fecha mínima para elegir al dia de hoy
            }
        )
    )
	hora = forms.TimeField(label="Hora", required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
	
	
    
    
   
    
    
   