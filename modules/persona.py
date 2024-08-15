#Creación de la clase persona
class Persona:
    def __init__(self, nro_doc, tipo_doc, nombre1, nombre2, apellido1, apellido2, fecha_nacimiento, lugar_expedicion, direccion, genero, rh, telefono, correo, tipo_poblacion, tipo_afiliacion, ocupacion, eps):
        self.__nro_doc = nro_doc
        self.__tipo_doc = tipo_doc
        self.__nombre1 = nombre1
        self.__nombre2 = nombre2
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__fecha_nacimiento = fecha_nacimiento
        self.__lugar_expedicion = lugar_expedicion
        self.__direccion = direccion
        self.__genero = genero
        self.__rh = rh
        self.__telefono = telefono
        self.__correo = correo
        self.__tipo_poblacion = tipo_poblacion
        self.__tipo_afiliacion = tipo_afiliacion
        self.__ocupacion = ocupacion
        self.__eps = eps

#getters&setters
    def get_nro_doc(self):
      return self.__nro_doc

    def set_nro_doc(self, nro_doc):
       self.__nro_doc = nro_doc

    def get_tipo_doc(self):
      return self.__tipo_doc

    def set_tipo_doc(self, tipo_doc):
       self.__tipo_doc = tipo_doc

    def get_nombre1(self):
      return self.__nombre1

    def set_nombre1(self, nombre1):
       self.__nombre1 = nombre1

    def get_nombre2(self):
      return self.__nombre2

    def set_nombre2(self, nombre2):
       self.__nombre2 = nombre2

    def get_apellido1(self):
      return self.__apellido1

    def set_apellido1(self, apellido1):
       self.__apellido1 = apellido1

    def get_apellido2(self):
      return self.__apellido2

    def set_apellido2(self, apellido2):
       self.__apellido2 = apellido2

    def get_fecha_nacimiento(self):
      return self.__fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
       self.__fecha_nacimiento = fecha_nacimiento

    def get_lugar_expedicion(self):
      return self.__lugar_expedicion

    def set_lugar_expedicion(self, lugar_expedicion):
       self.__lugar_expedicion = lugar_expedicion

    def get_direccion(self):
      return self.__direccion

    def set_direccion(self, direccion):
       self.__direccion = direccion

    def get_genero(self):
      return self.__genero

    def set_genero(self, genero):
       self.__genero = genero

    def get_rh(self):
      return self.__rh

    def set_rh(self, rh):
       self.__rh = rh

    def get_telefono(self):
      return self.__telefono

    def set_telefono(self, telefono):
       self.__telefono = telefono

    def get_correo(self):
      return self.__correo

    def set_correo(self, correo):
       self.__correo = correo

    def get_tipo_poblacion(self):
      return self.__tipo_poblacion

    def set_tipo_poblacion(self, tipo_poblacion):
       self.__tipo_poblacion = tipo_poblacion

    def get_tipo_afiliacion(self):
      return self.__tipo_afiliacion

    def set_tipo_afiliacion(self, tipo_afiliacion):
       self.__tipo_afiliacion = tipo_afiliacion

    def get_ocupacion(self):
      return self.__ocupacion

    def set_ocupacion(self, ocupacion):
       self.__ocupacion = ocupacion

    def get_eps(self):
      return self.__eps

    def set_eps(self, eps):
       self.__eps = eps
