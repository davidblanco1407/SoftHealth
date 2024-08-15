from .persona import Persona

#Creación de la subclase medico, que hereda de persona.py
class Medico(Persona):
    def __init__(self, nro_doc, tipo_doc, nombre1, nombre2, apellido1, apellido2, fecha_nacimiento, lugar_expedicion, direccion, genero, rh, telefono, correo, tipo_poblacion, tipo_afiliacion, ocupacion, eps, ):
        super().__init__(nro_doc, tipo_doc, nombre1, nombre2, apellido1, apellido2, fecha_nacimiento, lugar_expedicion, direccion, genero, rh, telefono, correo, tipo_poblacion, tipo_afiliacion, ocupacion, eps)