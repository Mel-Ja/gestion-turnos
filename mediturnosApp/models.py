from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=150, verbose_name="Email") 
    dni = models.IntegerField(verbose_name="Dni", unique=True)

    class Meta:
        abstract = True
        
    def nombre_completo(self):
        return f"{self.nombre}  {self.apellido}"


class Paciente(Persona):
    historia_clinica = models.CharField(verbose_name="Historia Clínica", primary_key=True, unique=True)
    
    def __str__(self):
        return f"{self.nombre_completo()}"

class Especialidad(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Especialidad", default='')
    descripcion = models.CharField(max_length=250, verbose_name="EspecialidadDescripcion", default='')
    imagen = models.ImageField(upload_to='images')
        
    def __str__(self):
        return f"{self.nombre}"


class Medico(Persona):
    matricula = models.CharField(max_length=50, primary_key=True, verbose_name="Matrícula")
    especialidades = models.ManyToManyField(Especialidad, through='MedicoEspecialidad')

    def __str__(self):
        return f"{self.nombre_completo()}"

class MedicoEspecialidad(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, db_column='matricula')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, db_column='especialidad_id')
    
    def __str__(self):
        return f"Médico: {self.medico.nombre_completo()} - Especialidad: {self.especialidad.descripcion}"
       
class Turnos(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cancelado = models.BooleanField()
    matricula = models.ForeignKey(Medico, on_delete=models.CASCADE)
    historia_clinica = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f" Paciente: {self.historia_clinica.nombre_completo()} Turno: {self.fecha} {self.hora} con el médico: {self.matricula.nombre_completo()}"