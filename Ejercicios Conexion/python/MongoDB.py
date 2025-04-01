#Instalar paquetes
# pip install pymongo

#Importamos libreria pymongo
import pymongo

try:
    #Conexion por local host
    cliente = pymongo.MongoClient("mongodb://localhost:27017/")

    #Si la conexion es exitosa
    print(cliente)
    print("\u2705 Conexion exitosa")
    
    #Imprime el tipo de objeto creado
    print(f"\U0001F50E Tipo de objeto de conexión: {type(cliente)}")

    #Listar todas las bases de datos disponibles en el servidor
    print("\U0001F4C1 Bases de datos disponibles: ", cliente.list_database_names())

    # Creamos o accedemos a la base de datos llamada "mydatabase"
    mibasededatos = cliente["ecommerce3066478"]

    # Creamos o accedemos a la coleccion llamada "mycolletion" dentro de la base datos
    micoleccion = mibasededatos["Clientes1"]

    # Documento que se insertara en la coleccion
    documento = {
        "Nombre": "Alice", 
        "Correo": "alice123@gmail.com",
        "telefono": "3183812699",
        "Direccion":"cra 22 #12 - 03",
        "Creado desde": "Python"
        }

    #Insertamos el documento en la coleccion
    resultado = micoleccion.insert_one(documento)

    # Imprimimos el ID del documento insertado

    print(f"\U0001F4CC Documento insertado con ID: {resultado.inserted_id}")

except Exception as err:
    print("\u274C Error:", err)   

finally:
    # Cerramos la conexion con servidor
    cliente.close()
    print(" \u2757 Conexion cerrada")