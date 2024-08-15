from persona import *

class PersonalHospital(Persona):
    personal = []

    def __init__(self, nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena, cargo):
        super().__init__(nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena)
        self.cargo = cargo

    @classmethod
    def registrarPersonal(cls, file='files/personal_hospital.txt'):
        nombre1 = input("Ingrese su primer nombre: ")
        nombre2 = input("Ingrese su segundo nombre: ")
        apellido1 = input("Ingrese su primer apellido: ")
        apellido2 = input("Ingrese su segundo apellido: ")
        td = int(input("Seleccione su tipo de documento:\n1. Cédula de Ciudadanía(Cc.)\n2. Tarjeta de Identidad(Ti.)\n3. Cédula de Extranjería(Ce.)\n4. Pasaporte"))
        while td < 1 or td > 4:
            td = int(input("Digite un tipo de documento válido"))
        if td == 1:
            tipoDocumento = 'CC'
        elif td == 2:
            tipoDocumento = 'TI'
        elif td == 3:
            tipoDocumento = 'CE'
        else:
            tipoDocumento = 'PA'
        documento = input("Ingrese su número de documento: ")
        fechaNacimiento = input("Ingrese su fecha de nacimiento, en formato DD/MM/AAAA: ")
        direccion = input("Digite su dirección de residencia: ")
        celular = input("Ingrese su número de celular, sin signos de puntuación o espacios: ")
        correo = input("Ingrese su correo electrónico: ").lower()
        contrasena = input("Digite su contraseña: ")
        while len(contrasena) < 8:
            contrasena = input("La contraseña debe tener mínimo 8 caracteres. Inténtelo de nuevo.")
        cargo = input("Ingrese su cargo (Ej. Médico, Enfermero, etc.): ")
        personal = cls(nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena, cargo)
        cls.personal.append(personal)
        with open(file, 'a', encoding='utf-8') as f:
            cadena = f"{nombre1}, {nombre2}, {apellido1}, {apellido2}, {tipoDocumento}, {documento}, {fechaNacimiento}, {direccion}, {celular}, {correo}, {contrasena}, {cargo}"
            f.write(cadena + '\n')
        return personal

    @classmethod
    def obtenerPersonal(cls, file='files/personal_hospital.txt'):
        personal = []
        with open(file, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            for l in lineas:
                nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena, cargo = l.strip().split(', ')
                personal.append(cls(nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena, cargo))
        return personal
