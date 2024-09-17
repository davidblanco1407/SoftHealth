#Importación de librerías
import pymongo

#Creación de la clase para la conexión a mongodb
class DBManager:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="softhealth"):
        self.cliente = pymongo.MongoClient(uri)
        self.db = self.cliente[db_name]

#Métodos crud
    def insertar(self, coleccion, doc):
        coleccion = self.db[coleccion]
        coleccion.insertOne(doc)

    def encontrar(self, coleccion, query, many=False):
        coleccion = self.db[coleccion]
        if many == False:
            return coleccion.findOne(query)
        return coleccion.find(query)

    def actualizar(self, coleccion, query, nuevo_valor):
        coleccion = self.db[coleccion]
        coleccion.updateOne(query, {"$set": nuevo_valor})

    def eliminar(self, coleccion, query):
        coleccion = self.db[coleccion]
        coleccion.deleteOne(query)

db_manager = DBManager()