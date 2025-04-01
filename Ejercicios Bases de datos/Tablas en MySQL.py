#Importamos el modulo para la conexion con MySQL
import mysql.connector

# Conectar a mySQL.
conn = mysql.connector.connect(  
    host="localhost",         #Direccion del servidor de la base de datos (en este caso, local)
    user="root",              #Usuario de MySQL
    password="",              #Contraseña del usuario de mySQL (debe configurarse si tiene una)
)
# Creamos cursor para la navegacion en tablas
cursor = conn.cursor()

# Crearla base de datos.
cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce3066478")

# Conectar a la base de datos creada.
conn.database = "ecommerce3066478"

# Crear tablas
tables = {
    "Clientes": """
        CREATE TABLE IF NOT EXISTS Clientes(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        correo VARCHAR(255) UNIQUE,
        telefono VARCHAR(255),
        direccion TEXT
        )
    """,
    "Productos": """
        CREATE TABLE IF NOT EXISTS Productos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        descripcion TEXT,
        precio DECIMAL(10,2),
        stock INT
        )
    """,
    "Ventas": """
        CREATE TABLE IF NOT EXISTS Ventas(
        id INT AUTO_INCREMENT PRIMARY KEY,
        cliente_id INT,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total DECIMAL(10,2),
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
        )
    """,
    "Detalle_ventas": """
        CREATE TABLE IF NOT EXISTS Detalle_ventas(
        id INT AUTO_INCREMENT PRIMARY KEY,
        venta_id INT,
        producto_id INT,
        cantidad INT,
        subtotal DECIMAL(10 ,2),
        FOREIGN KEY (venta_id) REFERENCES ventas(id),
        FOREIGN KEY (producto_id) REFERENCES productos(id)
        )
    """, 
    "Compras": """
        CREATE TABLE IF NOT EXISTS Compras(
        id INT AUTO_INCREMENT PRIMARY KEY,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total DECIMAL(10,2)
        )
    """,
    "Detalle_compras":"""
        CREATE TABLE IF NOT EXISTS Detalle_compras(
        id INT AUTO_INCREMENT PRIMARY KEY,
        compra_id INT,
        producto_id INT,
        cantidad INT,
        costo DECIMAL(10,2),
        FOREIGN KEY (compra_id) REFERENCES Compras(id),
        FOREIGN KEY (producto_id) REFERENCES Productos(id)
        )
    """   
}
for name, query in tables.items():
    cursor.execute(query)
    print(f"Tabla {name} creada. ")

cursor.close()
conn.close()