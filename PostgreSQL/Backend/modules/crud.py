from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(db):
    # Imprimir el título del módulo
    console.print(Panel.fit("🔧[bold cyan]Módulo CRUD Básico[/bold cyan] 🔧"))

    # Crear las tablas si no existen
    with db.get_cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            descripcion TEXT
        );
        """)
        
        cur.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            precio NUMERIC NOT NULL,
            categoria_id INTEGER REFERENCES categorias(id) ON DELETE SET NULL,
            stock INTEGER,
            descripcion TEXT
        );
        """)
        db.conn.commit()

    # Insertar datos en las tablas, con manejo de posibles conflictos
    with db.get_cursor() as cur:
        # Insertar categoría si no existe
        cur.execute("""
        INSERT INTO categorias (nombre, descripcion) VALUES
        ('Libros', 'Categoría de libros')
        ON CONFLICT DO NOTHING;
        """)
        
        # Insertar producto si no existe
        cur.execute("""
        INSERT INTO productos (nombre, precio, categoria_id, stock, descripcion) VALUES
        ('Libro Python', 39000, 1, 25, 'Guía práctica de Python')
        ON CONFLICT DO NOTHING;
        """)

        # Confirmar los cambios
        db.conn.commit()

        # Recuperar todos los productos
        cur.execute("SELECT * FROM productos")
        rows = cur.fetchall()

        # Crear la tabla de resultados
        table = Table(title="Productos")
        
        # Añadir columnas a la tabla basadas en las claves de la primera fila
        for col in rows[0].keys():
            table.add_column(col)
        
        # Añadir las filas a la tabla
        for row in rows:
            table.add_row(*[str(v) for v in row.values()])

        # Imprimir la tabla en la consola
        console.print(table)
