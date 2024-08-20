from simple_colors import *
from persona import *

class Administrador(Persona):
    administradores = []
    def __init__(self, nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena):
        super().__init__(nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena)

    @classmethod
    def registrarAdmin(cls, file='files/administradores.txt'):
        print('-'*80)
        print(green(f'{'-'*25} Registro Administrador {'-'*25}','bold'))
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
        admin = cls(nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena)
        cls.administradores.append(admin)
        with open(file, 'a', encoding='utf-8') as f:
            cadena = f'{nombre1}, {nombre2}, {apellido1}, {apellido2}, {tipoDocumento}, {documento}, {fechaNacimiento}, {direccion}, {celular}, {correo}, {contrasena}'
            f.write(cadena + '\n')
        return admin

    @classmethod
    def obtenerAdmin(cls, file='files/administradores.txt'):
        administradores = []
        with open(file, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            for l in lineas:
                nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena = l.strip().split(', ')
                administradores.append(cls(nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena))
        return administradores
    
    def iniciarSesion(cls, file='files/administradores.txt'):
        print('-'*80)
        correo = input('    >>> Ingrese su correo electrónico: ').lower()
        contrasena = input('    >>> Digite su contraseña: ')
        administradores = cls.obtenerAdmin(file)
        for admin in administradores:
            if admin.getCorreo() == correo and admin.getContrasena() == contrasena:
                print(yellow('\n',admin.getNombre1(), admin.getApellido1(),' esta iniciando sesión...'))
                input(green('Inicio de sesión correcto, "enter" para continuar '))
                return True
            else:
                return False