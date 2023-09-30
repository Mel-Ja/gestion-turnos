from django import forms
from datetime import datetime, timedelta

class SolicitarTurnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Nombre'}))
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Apellido'}))
    dni = forms.CharField(label="DNI", required=True, widget=forms.TextInput(attrs={'class': 'form-control dni-input', 'pattern': '[0-9]{8}', 'title': 'El DNI debe contener 8 dígitos numéricos', 'maxlength': '8', 'placeholder': 'DNI'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    especialidad = forms.CharField(label="Especialidad", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Especialidad'}))
    medico = forms.CharField(label="Médico", required=True, widget=forms.TextInput(attrs={'class': 'form-control solo-letras', 'placeholder': 'Médico'}))
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
