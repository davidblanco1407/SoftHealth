# forms.py
from django import forms
from django.db import transaction
from .models import Paciente, Medico, HistoriaClinica, User,  Auxiliar, CitaMedica, EPS


class PacienteFormulario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
        model = Paciente
        fields = ['nombre', 'tipo_documento', 'documento', 'correo', 'fecha_nacimiento', 'eps', 'password']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    

    def save(self, commit=True):
        paciente = super().save(commit=False)

        # Verifica si el paciente ya tiene un User asociado
        if paciente.user:
            # Actualiza el User existente
            user = paciente.user
            user.username = self.cleaned_data['nombre']
            if self.cleaned_data['password']:  # Actualiza la contraseña solo si se proporciona
                user.set_password(self.cleaned_data['password'])
            user.save()
        else:
            # Crea un nuevo User si no existe uno asociado
            user = User.objects.create_user(
                username=self.cleaned_data['nombre'],
                password=self.cleaned_data['password']
            )
            paciente.user = user

        if commit:
            paciente.save()  # Guarda el paciente

        return paciente


class MedicoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
        model = Medico
        fields = ['nombre', 'tipo_documento', 'documento', 'especialidad','password']

    

    def save(self, commit=True):
        medico = super().save(commit=False)

        # Verifica si el medico ya tiene un User asociado
        if medico.user:
            # Actualiza el User existente
            user = medico.user
            user.username = self.cleaned_data['nombre']
            if self.cleaned_data['password']:  # Actualiza la contraseña solo si se proporciona
                user.set_password(self.cleaned_data['password'])
            user.save()
        else:
            # Crea un nuevo User si no existe uno asociado
            user = User.objects.create_user(
                username=self.cleaned_data['nombre'],
                password=self.cleaned_data['password']
            )
            medico.user = user

        if commit:
            medico.save()  # Guarda el medico

        return medico

class HistoriaClinicaFormulario(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['diagnostico', 'tratamiento', 'observaciones']  # Excluir 'fecha_creacion'


class BuscarHistoriaClinicaForm(forms.Form):
    identificacion = forms.CharField(label="Número de Identificación", max_length=20, required=True)


class AuxiliarFormulario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Auxiliar
        fields = ['nombre', 'documento', 'correo', 'password']

    def save(self, commit=True):
        aux = super().save(commit=False)

        # Verifica si el Auxiliar ya tiene un User asociado
        if aux.user:
            # Actualiza el User existente
            user = aux.user
            user.username = self.cleaned_data['nombre']
            if self.cleaned_data['password']:  # Actualiza la contraseña solo si se proporciona
                user.set_password(self.cleaned_data['password'])
            user.save()
        else:
            # Crea un nuevo User si no existe uno asociado
            user = User.objects.create_user(
                username=self.cleaned_data['nombre'],
                password=self.cleaned_data['password']
            )
            aux.user = user

        if commit:
            aux.save()  # Guarda el Auxiliar

        return aux


class CitaMedicaFormulario(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['paciente', 'medico', 'fecha', 'hora', 'motivo']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }


class EpsForm(forms.ModelForm):
    class Meta:
        model = EPS
        fields = ['codigo', 'nombre_eps', 'telefono', 'direccion', 'correo_electronico']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
