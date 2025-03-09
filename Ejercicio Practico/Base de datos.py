#Importamos libreria pymongo
from pymongo import MongoClient

# Conectar con MongoDB.
client = MongoClient("mongodb://localhost:27017/")

# Crear base de datos
db = client["Sena"]

coleccion = db["Estudiantes"]

# Creamos 5 documentos para insertar en la coleccion

Estudiantes = [
    {"Nombres": "Esteban", "Apellidos": "Garzón Amaya", "Edad": 27,"Curso": "Análisis y Desarrollo de Software", "Nota": 9.5},
    {"Nombres": "Ana", "Apellidos": "Martínez López", "Edad": 19,"Curso": "Entrenamiento Deportivo", "Nota": 8.7},
    {"Nombres": "Carlos", "Apellidos": "Pérez Ramírez", "Edad": 22,"Curso": "Análisis y Desarrollo de Software", "Nota": 5.8},
    {"Nombres": "Laura", "Apellidos": "Fernández Gómez", "Edad": 18,"Curso": "Entrenamiento Deportivo", "Nota": 8.9},
    {"Nombres": "Miguel", "Apellidos": "Torres Jiménez", "Edad": 26,"Curso": "Produccion Agropecuaria", "Nota": 6.8}
]

# Insertar los documentos en la coleccion

coleccion.insert_many(Estudiantes)







