from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=150, verbose_name="Email") 
    dni = models.IntegerField(verbose_name="Dni", unique=True)

    class Meta:
        abstract = True

class Especialidad(models.Model):
    descripcion = models.CharField(max_length=250, verbose_name="Especialidad")

class Paciente(Persona):
    historia_clinica = models.CharField(verbose_name="Historia Clínica", primary_key=True)

class Medico(Persona):
    matricula = models.CharField(verbose_name="Matrícula", primary_key=True)
    especialidad = models.ManyToManyField(Especialidad)

class Turnos(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cancelado = models.BooleanField()
    matricula = models.ForeignKey(Medico, on_delete=models.CASCADE)
    historia_clinica = models.ForeignKey(Paciente, on_delete=models.CASCADE)