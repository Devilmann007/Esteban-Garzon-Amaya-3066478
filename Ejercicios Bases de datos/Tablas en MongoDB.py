#Importamos libreria pymongo
from pymongo import MongoClient

# Conectar con MongoDB.
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce3066478"]

# Crear colecciones 
clientes =db["Clientes1"]
productos =db["Productos1"]
ventas =db["Ventas1"]
compras =db["Compras1"]
compras =db["Comercio1"]

# Insertar documentos de ejemplo
clientes.insert_one({"Nombre": "Esteban Garzon", "Correo": "acid.mann@outlook.com", "Telefono": "3195151378", "Direccion": "Cll 17a # 13c-10" })
productos.insert_one({"Nombre": "Laptop", "Descripcion": "Laptop Lenovo alta gama", "Precio": 1200, "Stock": 10})

print("Base de datos y colecciones creadas en MongoDB")