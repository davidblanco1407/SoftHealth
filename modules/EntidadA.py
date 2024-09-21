from .db import *

class Entidad:
    entidades = []

    def __init__(self, nombre, nit, categoria, serviciosOfrecidos, direccion):
        self.__nombre = nombre
        self.__nit = nit
        self.__categoria = categoria
        self.__serviciosOfrecidos = serviciosOfrecidos
        self.__direccion = direccion

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNit(self):
        return self.__nit

    def setNit(self, nit):
        self.__nit = nit

    def getCategoria(self):
        return self.__categoria

    def setCategoria(self, categoria):
        self.__categoria = categoria

    def getServiciosOfrecidos(self):
        return self.__serviciosOfrecidos

    def setServiciosOfrecidos(self, serviciosOfrecidos):
        self.__serviciosOfrecidos = serviciosOfrecidos

    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        self.__direccion = direccion

    @classmethod
    def registrarEntidad(cls):
        print('Sobre la IPS/EPS: ', '☲' * 40)
        nombre = input('Ingrese el nombre de la IPS/EPS: ')
        nit = input('Ingrese el NIT de la IPS/EPS: ')
        categoria = input('Ingrese la categoría de la IPS/EPS (I, II, III, IV, V): ').upper()
        while categoria not in ['I', 'II', 'III', 'IV', 'V']:
            categoria = input('Ingrese una categoría válida (I, II, III, IV, V): ').upper()

        # Definir los servicios ofrecidos según la categoría
        serviciosOfrecidos = cls._definirServicios(categoria)

        direccion = input('Ingrese la dirección de la IPS/EPS: ')
        nuevaEntidad = cls(nombre, nit, categoria, serviciosOfrecidos, direccion)
        cls.entidades.append(nuevaEntidad)
        doc_entidad = {
            'nombre': nombre,
            'nit': nit,
            'categoria': categoria,
            'direccion': direccion,
            'serviciosOfrecidos': serviciosOfrecidos
        }
        db_manager.insertar("Entidades", doc_entidad)
        return nuevaEntidad

    @classmethod
    def obtenerEntidades(cls):
        entidades = []
        resultados = db_manager.encontrar("Administradores", {}, True)
        for doc in resultados:
            entidad = cls(
                doc["nombre"], doc["nit"], doc["categoria"], doc["direccion"], doc["serviciosOfrecidos"]
            )
            entidades.append(entidad)
        return entidades

    @staticmethod
    def _definirServicios(categoria):
        servicios = {
            'I': 'Consulta médica general, Atención preventiva, Atención de enfermedades comunes, Tratamientos ambulatorios, Servicios de salud materno-infantil',
            'II': 'Consulta médica general, Consulta especializada, Diagnóstico básico, Tratamiento ambulatorios y hospitalización breve, Servicios de urgencias, Rehabilitación básica, Atención en salud mental',
            'III': 'Consulta médica general, Consulta especializada, Diagnostico avanzado, Urgencias, Tratamientos básicos, Cirugía general, Hospitalización, Atención preventiva',
            'IV': 'Consulta médica general, Consulta especializada, Diagnostico avanzado, Tratamientos especializados, Cirugía Especializada, Unidades de cuidados intensivos (UCI), Rehabilitación avanzada',
            'V': 'Consulta médica general, Consulta altamente especializada, Diagnóstico de alta tecnología, Urgencias críticas, Tratamientos avanzados, Cirugía de alta complejidad, Investigación clínica, Unidades de cuidados intensivos (UCI)'
        }
        return servicios.get(categoria, '')

