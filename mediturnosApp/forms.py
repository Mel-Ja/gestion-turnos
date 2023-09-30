from django import forms	
	
class SolicitarTurnoForm(forms.Form):	
	
	nombre = forms.CharField(label="Nombre", required=True)
	apellido = forms.CharField(label="Apellido", required=True)
	dni = forms.CharField(label="Dni", required=True)
	email = forms.EmailField(label="Email", required=True)
	Especialidad = forms.CharField(label="Especialidad", required=True)
	Medico = forms.CharField(label="Medico", required=True)
	fecha = forms.DateField(label="Fecha", required=True, widget=forms.DateInput(attrs={'type': 'date'}))
	hora = forms.TimeField(label="Hora", required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
	
	
