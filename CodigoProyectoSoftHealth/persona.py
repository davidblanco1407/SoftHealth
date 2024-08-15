class Persona:
    def __init__(self, nombre1, nombre2, apellido1, apellido2, tipoDocumento, documento, fechaNacimiento, direccion, celular, correo, contrasena):
        self.__nombre1 = nombre1
        self.__nombre2 = nombre2
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__tipoDocumento = tipoDocumento
        self.__documento = documento
        self.__fechaNacimiento = fechaNacimiento
        self.__direccion = direccion
        self.__celular = celular
        self.__correo = correo
        self.__contrasena = contrasena

    def getNombre1(self):
      return self.__nombre1

    def setNombre1(self, nombre1):
       self.__nombre1 = nombre1

    def getNombre2(self):
      return self.__nombre2

    def setNombre2(self, nombre2):
       self.__nombre2 = nombre2

    def getApellido1(self):
      return self.__apellido1

    def setApellido1(self, apellido1):
       self.__apellido1 = apellido1

    def getApellido2(self):
      return self.__apellido2

    def setApellido2(self, apellido2):
       self.__apellido2 = apellido2

    def get_tipoDocumento(self):
      return self.__tipoDocumento

    def set_tipoDocumento(self, tipoDocumento):
       self.__tipoDocumento = tipoDocumento

    def getDocumento(self):
      return self.__documento

    def setDocumento(self, documento):
       self.__documento = documento

    def get_fechaNacimiento(self):
      return self.__fechaNacimiento

    def set_fechaNacimiento(self, fechaNacimiento):
       self.__fechaNacimiento = fechaNacimiento

    def getDireccion(self):
      return self.__direccion

    def setDireccion(self, direccion):
       self.__direccion = direccion

    def getCelular(self):
      return self.__celular

    def setCelular(self, celular):
       self.__celular = celular

    def getCorreo(self):
      return self.__correo

    def setCorreo(self, correo):
       self.__correo = correo

    def getContrasena(self):
      return self.__contrasena

    def setContrasena(self, contrasena):
       self.__contrasena = contrasena
