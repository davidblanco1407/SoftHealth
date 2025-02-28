from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    PacienteFormulario,
    MedicoForm,
    HistoriaClinicaFormulario,
    BuscarHistoriaClinicaForm,
    AuxiliarFormulario,
    CitaMedicaFormulario,
    EpsForm,
    LoginForm,
)
from django.contrib import messages
from django.http import HttpResponse
from .forms import PacienteFormulario
from .models import Paciente, Medico, HistoriaClinica, Auxiliar, CitaMedica, EPS
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

@login_required
def home_redirect(request):
    """Redirige al usuario al inicio correspondiente según su rol."""

    if Paciente.objects.filter(user=request.user).exists():
        return redirect('inicio_paciente')  # Redirige a la página de inicio del paciente

    if Medico.objects.filter(user=request.user).exists():
        return redirect('inicio_medico')  # Redirige a la página de inicio del médico

    if Auxiliar.objects.filter(user=request.user).exists():
        return redirect('inicio_aux_administrativo')  # Redirige a la página de inicio del auxiliar

    return redirect('home')  # Redirige a la página de inicio general si no tiene rol

# LOGIN PACIENTE
def login_paciente(request):
    mensaje_error = ""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Extraer credenciales
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Autenticar usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Iniciar sesión del usuario
                login(request, user)
                return redirect('inicio_paciente')
            else:
                # Mostrar mensaje de error
                mensaje_error = "Credenciales incorrectas. Por favor, inténtelo de nuevo."
    else:
        form = LoginForm()

    return render(request, 'Paciente/login_paciente.html', {'form': form, 'mensaje_error': mensaje_error})


def login_medico(request):
    mensaje_error = ""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Extraer credenciales
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Autenticar usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Iniciar sesión del usuario
                login(request, user)
                return redirect('inicio_medico')
            else:
                # Mostrar mensaje de error
                mensaje_error = "Credenciales incorrectas. Por favor, inténtelo de nuevo."
    else:
        form = LoginForm()

    return render(request, 'Medico/login_medico.html', {'form': form, 'mensaje_error': mensaje_error})

def login_aux_administrativo(request):
    mensaje_error = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Autenticar usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Iniciar sesión del usuario
                login(request, user)
                return redirect('inicio_aux_administrativo')
            else:
                # Mostrar mensaje de error
                mensaje_error = "Credenciales incorrectas. Por favor, inténtelo de nuevo."
    else:
        form = LoginForm()
    return render(request, 'Aux_Administrativo/login_aux_administrativo.html', {'form': form, 'mensaje_error':mensaje_error})

# @login_required(login_url='home')
# PACIENTE

# Insertar Pacientes
def insertar_paciente(request):
    mensaje_error = ""

    eps_list = EPS.objects.all()
    if request.method == 'POST':
        form = PacienteFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_paciente')
        else:
            mensaje_error = "El usuario ya se encuentra registrado. Por favor, inténtelo de nuevo."
    else:
        form = PacienteFormulario()
    return render(request, 'Paciente/insertar_paciente.html', {'form': form, 'eps_list': eps_list, 'mensaje_error':mensaje_error})


# Listar Pacientes
def listar_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'Paciente/listar_paciente.html', {'pacientes': pacientes})


# Eliminar Paciente
def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    messages.success(request, 'Médico eliminado correctamente.')
    return redirect('listar_paciente')


# Actualizar Paciente
@login_required(login_url='login')
def actualizar_paciente(request, id):
    # Obtén el paciente específico por su ID
    paciente = get_object_or_404(Paciente, id=id)
    eps_list=EPS.objects.all()
    if request.method == 'POST':
        
        form = PacienteFormulario(request.POST, instance=paciente)
        if form.is_valid():
            
            try:
                form.save()
                return redirect('listar_paciente')
            except Exception as e:
                messages.error(request, f'Error al actualizar el paciente: {str(e)}')
        else:
            # Imprime los errores del formulario en la consola
            print(form.errors)
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        messages.error(request, f'{str(request.method)}')
        form = PacienteFormulario(instance=paciente)

    return render(request, 'Paciente/actualizar_paciente.html', {
        'form': form,
        'paciente': paciente,
        'eps_list': eps_list,
    })


# Inicio Paciente
def inicio_paciente(request):
    paciente = Paciente.objects.filter(user=request.user).first()  # Obtener el paciente asociado al usuario

    if not paciente:
        return redirect('home')  # Redirigir si no se encuentra paciente

    context = {
        'paciente': paciente
    }
    return render(request, 'Paciente/inicio_paciente.html', context)


# MEDICO

# Insertar Medico
def insertar_medico(request):
    mensaje_error = ""

    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medico')
        else:
            mensaje_error = "El usuario ya se encuentra registrado. Por favor, inténtelo de nuevo."
    else:
        form = MedicoForm()
    return render(request, 'Medico/insertar_medico.html', {'form': form, 'mensaje_error':mensaje_error})


# Listar Médicos
def listar_medico(request):
    medicos = Medico.objects.all()
    return render(request, 'Medico/listar_medico.html', {'medicos': medicos})


# Eliminar Médico
def eliminar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    medico.delete()
    messages.success(request, 'Médico eliminado correctamente.')
    return redirect('listar_medico')


# Actualizar Médico
@login_required(login_url='login')
def actualizar_medico(request, id):
    # Obtén el medico específico por su ID
    medico = get_object_or_404(Medico, id=id)

    if request.method == 'POST':
        
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            
            try:
                form.save()
                return redirect('listar_medico')
            except Exception as e:
                messages.error(request, f'Error al actualizar el medico: {str(e)}')
        else:
            # Imprime los errores del formulario en la consola
            print(form.errors)
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        messages.error(request, f'{str(request.method)}')
        form = MedicoForm(instance=medico)

    return render(request, 'Medico/actualizar_medico.html', {
        'form': form,
        'medico': medico,
    })

# Inicio Médico
def inicio_medico(request):
    medico = Medico.objects.first()
    return render(request, 'Medico/inicio_medico.html', {'medico': medico})


# Seleccionar Paciente
def seleccionar_paciente(request):
    paciente = Paciente.objects.all()
    return render(request, 'Medico/seleccionar_paciente.html', {'paciente': paciente})

# Seleccionar Paciente
def seleccionar_paciente_2(request):
    paciente = Paciente.objects.all()
    return render(request, 'Medico/seleccionar_paciente_2.html', {'paciente': paciente})


# HISTORIA CLÍNICA

# Insertar Historia Clínica
def insertar_historia_clinica(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = HistoriaClinicaFormulario(request.POST)
        if form.is_valid():
            historia_clinica = form.save(commit=False)
            historia_clinica.paciente = paciente
            historia_clinica.save()
            return redirect('listar_historia_clinica')
    else:
        form = HistoriaClinicaFormulario()
    return render(request, 'Historia_Clinica/insertar_historia_clinica.html', {'form': form, 'paciente': paciente})

# Listar Historia Clínica
def listar_historia_clinica(request):
    historias = HistoriaClinica.objects.all()
    return render(request, 'Historia_Clinica/listar_historia_clinica.html', {'historias': historias})

def listar_historia_clinica_2(request, paciente_id):
     # Obtén el paciente según el ID proporcionado
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    # Obtén las historias clínicas asociadas al paciente
    historias = HistoriaClinica.objects.filter(paciente=paciente)
    
    # Renderiza la plantilla con los datos
    return render(request, 'Historia_Clinica/listar_historia_clinica_2.html', {
        'historias': historias,
        'paciente': paciente,
    })

# Eliminar Historia Clínica
def eliminar_historia_clinica(request, id):
    historia = get_object_or_404(HistoriaClinica, id=id)
    historia.delete()
    return redirect('listar_historias_clinicas')


# AUXILIAR

# Insertar Auxiliar
def insertar_auxiliar(request):
    mensaje_error = ""
    if request.method == 'POST':
        form = AuxiliarFormulario(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Auxiliar registrado correctamente.')
                return redirect('listar_auxiliares')
            except Exception as e:
                mensaje_error = f"Error al registrar el auxiliar: {str(e)}"
        else:
            # Imprime los errores del formulario en la consola
            print(form.errors)
            mensaje_error = "Por favor, corrige los errores en el formulario."
    else:
        form = AuxiliarFormulario()

    return render(request, 'Aux_Administrativo/insertar_auxiliar.html', {
        'form': form,
        'mensaje_error': mensaje_error,
    })


# Listar Auxiliar
def listar_auxiliares(request):
    auxiliares = Auxiliar.objects.all()
    return render(request, 'Aux_Administrativo/listar_auxiliares.html', {'auxiliares': auxiliares})

@login_required(login_url='login')
def actualizar_auxiliar(request, id):
    # Obtén el auxiliar específico por su ID
    auxiliar = get_object_or_404(Auxiliar, id=id)

    if request.method == 'POST':
        form = AuxiliarFormulario(request.POST, instance=auxiliar)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Datos del auxiliar actualizados correctamente.')
                return redirect('listar_auxiliares')
            except Exception as e:
                messages.error(request, f'Error al actualizar el auxiliar: {str(e)}')
        else:
            # Imprime los errores del formulario en la consola
            print(form.errors)
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = AuxiliarFormulario(instance=auxiliar)

    return render(request, 'Aux_Administrativo/actualizar_auxiliar.html', {
        'form': form,
        'auxiliar': auxiliar,
    })

# Eliminar Auxiliar
def eliminar_auxiliar(request, id):
    auxiliar = get_object_or_404(Auxiliar, id=id)
    auxiliar.delete()
    return redirect('listar_auxiliares')


# Inicio
def inicio_aux_administrativo(request):
    return render(request, 'Aux_Administrativo/inicio_aux_administrativo.html')


# CITA MÉDICA
def insertar_cita(request):
    pacientes = Paciente.objects.all  # Obtén el paciente específico
    medicos = Medico.objects.all()  # Obtener la lista de médicos

    if request.method == 'POST':
        form = CitaMedicaFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')  # Cambiar según tu URL de redirección
    else:
        form = CitaMedicaFormulario()

    context = {
        'form': form,
        'pacientes': pacientes,
        'medicos': medicos,
    }

    return render(request, 'Cita/insertar_cita.html', context)

def insertar_cita_2(request):
    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()  # Obtener la lista de médicos
    
    if request.method == 'POST':
        form = CitaMedicaFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')  # Cambiar según tu URL de redirección
    else:
        form = CitaMedicaFormulario()

    return render(request, 'Cita/insertar_cita_2.html', {
        'form': form,
        'pacientes':pacientes,
        'medicos': medicos,
    })

def listar_citas(request):
    citas = CitaMedica.objects.all()
    return render(request, 'Cita/listar_cita.html', {'citas': citas})


def eliminar_cita(request, id):
    cita = get_object_or_404(CitaMedica, id=id)
    cita.delete()
    messages.success(request, "Cita médica eliminada exitosamente.")
    return redirect('listar_citas')

# EPS
def insertar_eps(request):
    if request.method == 'POST':
        form = EpsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eps')
    else:
        form = EpsForm()
    return render(request, 'Eps/insertar_eps.html', {'form': form})


def listar_eps(request):
    eps_list = EPS.objects.all()
    return render(request, 'Eps/listar_eps.html', {'eps_list': eps_list})


def eliminar_eps(request, id):
    eps = get_object_or_404(EPS, id=id)
    eps.delete()
    return redirect('listar_eps')

def actualizar_eps(request, id):
    eps = get_object_or_404(EPS, id=id)
    if request.method == 'POST':
        form = EpsForm(request.POST, instance=eps)
        if form.is_valid():
            form.save()
            return redirect('listar_eps')
    else:
        form = EpsForm(instance=eps)
    return render(request, 'eps/actualizar_eps.html', {'form': form, 'eps': eps})