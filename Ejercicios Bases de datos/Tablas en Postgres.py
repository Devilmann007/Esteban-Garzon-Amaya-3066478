# Importamos PostgreSQL
import psycopg2

# Conectar a PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Psql2025",
    host="localhost"
)
conn.autocommit = True
cursor = conn.cursor()

# Crear base de datos.
cursor.execute("CREATE DATABASE ecommerce3066478")
cursor.close()  # Cerrar conexion para conectar con la nueva base

# Conectar con la nueva base de datos.
conn = psycopg2.connect(
    dbname="ecommerce3066478",
    user="postgres",
    password="Psql2025",
    host="localhost"
)
cursor = conn.cursor()

# Crear tablas
tables = {
    "Clientes": """
        CREATE TABLE IF NOT EXISTS Clientes (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255),
            correo VARCHAR(255) UNIQUE,
            telefono VARCHAR(255),
            direccion TEXT
        )
    """,
    "Productos": """
        CREATE TABLE IF NOT EXISTS Productos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255),
            descripcion TEXT,
            precio DECIMAL(10,2),
            stock INT
        )
    """,
    "Ventas": """
        CREATE TABLE IF NOT EXISTS Ventas (
            id SERIAL PRIMARY KEY,
            cliente_id INT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total DECIMAL(10,2),
            FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
        )
    """,
    "Detalle_ventas": """
        CREATE TABLE IF NOT EXISTS Detalle_ventas (
            id SERIAL PRIMARY KEY,
            venta_id INT,
            producto_id INT,
            cantidad INT,
            subtotal DECIMAL(10,2),
            FOREIGN KEY (venta_id) REFERENCES Ventas(id),
            FOREIGN KEY (producto_id) REFERENCES Productos(id)
        )
    """,
    "Compras": """
        CREATE TABLE IF NOT EXISTS Compras (
            id SERIAL PRIMARY KEY,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total DECIMAL(10,2)
        )
    """,
    "Detalle_compras": """
        CREATE TABLE IF NOT EXISTS Detalle_compras (
            id SERIAL PRIMARY KEY,
            compra_id INT,
            producto_id INT,
            cantidad INT,
            costo DECIMAL(10,2),
            FOREIGN KEY (compra_id) REFERENCES Compras(id),
            FOREIGN KEY (producto_id) REFERENCES Productos(id)
        )
    """
}

# Ejecutar las consultas para crear las tablas
for name, query in tables.items():
    cursor.execute(query)
    print(f"Tabla {name} creada.")

# Confirmar los cambios y cerrar la conexión
conn.commit()
cursor.close()
conn.close()
