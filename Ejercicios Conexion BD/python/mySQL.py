# Importamos el módulo para la conexión con MySQL
import mysql.connector

try:
    # Establece conexión con la base de datos XAMPP
    conn = mysql.connector.connect(  
        host="localhost",         # Dirección del servidor de la base de datos (en este caso, local)
        user="root",              # Usuario de MySQL
        password="",              # Contraseña del usuario de MySQL (debe configurarse si tiene una)
        database="ecommerce3066478",  # Conectar a una base de datos específica
    ) 

    # Si la conexión se establece correctamente, imprimir un mensaje de éxito
    print(conn)
    print("\u2705 Conexion exitosa")
    print(f"\U0001F50E Tipo de objeto de conexión: {type(conn)}")  # Muestra el tipo de objeto de conexión

    # Creamos un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Ejecutamos una consulta SQL para listar las bases de datos en el servidor
    cursor.execute("SHOW DATABASES;")  # Corrección aquí, el nombre correcto es "SHOW DATABASES"

    # Iteramos sobre los resultados y los imprimimos
    for db in cursor:
        print(db)

except mysql.connector.Error as err:
    # Capturamos cualquier error de conexión y lo imprime
    print(f"\u2705 Error al conectar con MySQL: {err}")

finally:
    # Cerramos la conexión si se estableció correctamente
    if "conn" in locals() and conn.is_connected():
        cursor.close()  # Cerramos el cursor
        conn.close()  # Cerramos la conexión
        print(" \u2757 Conexion cerrada")
