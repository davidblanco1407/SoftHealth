# models.py
from django.contrib.auth.models import User
from django.db import models


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=2, choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula Extranjera')])
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    eps = models.ForeignKey('EPS', on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=2, choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula Extranjera')])
    documento = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre


class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    observaciones = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)  # Remover editable=False


    def __str__(self):
        return f"Historia de {self.paciente.nombre}"


class Auxiliar(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre


class CitaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita de {self.paciente.nombre} con {self.medico.nombre}"


class EPS(models.Model):
    codigo = models.CharField(max_length=10, null=True, blank=True)
    nombre_eps = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    correo_electronico = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre_eps

