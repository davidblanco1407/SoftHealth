from simple_colors import *
from .persona import *
from .db import *

class Paciente(Persona):
    def __init__(self, nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena):
        super().__init__(nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena)

    @classmethod
    def registrarPaciente(cls):
        print('-'*80)
        print(green(f'{'-'*25} Registro Paciente {'-'*25}','bold'))
        print('-'*80)
        nombre1 = input('    >>> Ingrese su primer nombre: ')
        nombre2 = input('    >>> Ingrese su segundo nombre: ')
        apellido1 = input('    >>> Ingrese su primer apellido: ')
        apellido2 = input('    >>> Ingrese su segundo apellido: ')
        print(black('Tipo de documento:\n1. Cédula de Ciudadanía(Cc.)\n2. Tarjeta de Identidad(Ti.)\n3. Cédula de Extranjería(Ce.)\n4. Pasaporte'))
        td = int(input('    >>> Seleccione una opción: '))
        while td < 1 or td > 4:
            td = int(input('Digite un tipo de documento válido'))
        if td == 1:
            tipoDocumento = 'CC'
        elif td == 2:
            tipoDocumento = 'TI'
        elif td == 3:
            tipoDocumento = 'CE'
        else:
            tipoDocumento = 'PA'
        documento = input('\n    >>> Ingrese su número de documento: ')
        fechaNacimiento = input('Ingrese su fecha de nacimiento, en formato DD/MM/AAAA: ')
        direccion = input('    >>> Digite su dirección de residencia: ')
        celular = input('    >>> Ingrese su número de celular, sin signos de puntuación o espacios: ')
        correo = input('    >>> Ingrese su correo electrónico: ').lower()
        contrasena = input('    >>> Dígite su contraseña: ')
        while len(contrasena) < 8:
            print(red('-'*80))
            print(red(f'{'-'*17} La contraseña debe tener mínimo 8 caracteres {'-'*17}'))
            print(red('-'*80))
            contrasena = input(('    >>> Inténtelo de nuevo: '))
        paciente = cls(nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena)
        doc_paciente = {
            "nombre1": nombre1,
            "nombre2": nombre2,
            "apellido1": apellido1,
            "apellido2": apellido2,
            "tipoDocumento": tipoDocumento,
            "documento": documento,
            "fechaNacimiento": fechaNacimiento,
            "direccion": direccion,
            "celular": celular,
            "correo": correo,
            "contrasena": contrasena
        }
        db_manager.insertar("Pacientes", doc_paciente)
        return paciente

    @classmethod
    def obtenerPaciente(cls):
        pacientes = []
        resultados = db_manager.encontrar("Pacientes", {}, True)
        for doc in resultados:
            paciente = cls(
                doc["nombre1"], doc["nombre2"], doc["apellido1"], doc["apellido2"],
                doc["tipoDocumento"], doc["documento"], doc["fechaNacimiento"],
                doc["direccion"], doc["celular"], doc["correo"], doc["contrasena"]
            )
            pacientes.append(paciente)
        return pacientes

    @classmethod
    def iniciarSesion(cls):
        print('-'*80)
        correo = input('    >>> Ingrese su correo electrónico: ').lower()
        contrasena = input('    >>> Digite su contraseña: ')
        pacientes = cls.obtenerPaciente()
        for paciente in pacientes:
            if paciente.getCorreo() == correo and paciente.getContrasena() == contrasena:
                print(yellow(f'\n{paciente.getNombre1()}, {paciente.getApellido1()}, esta iniciando sesión...'))
                input(green('Inicio de sesión correcto, "enter" para continuar '))
                return True
        print(red('Correo o contraseña incorrectos.'))
        return False