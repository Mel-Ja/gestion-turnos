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
    


class Especialidad(models.Model):
    descripcion = models.CharField(max_length=250, verbose_name="Especialidad")
    
    def __str__(self):
        return self.descripcion


class Medico(Persona):
    matricula = models.CharField(max_length=50, primary_key=True, verbose_name="Matrícula")
    especialidades = models.ManyToManyField(Especialidad, through='MedicoEspecialidad')


class MedicoEspecialidad(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, db_column='matricula')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, db_column='especialidad_id')
    
    
class Turnos(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cancelado = models.BooleanField()
    matricula = models.ForeignKey(Medico, on_delete=models.CASCADE)
    historia_clinica = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    