from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(db):
    # Mostrar el título del módulo
    console.print(Panel.fit("📌[bold cyan]Gestión de Índices[/bold cyan] 📌"))
    
    with db.get_cursor() as cur:
        # Crear el índice si no existe
        cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_productos_precio ON productos(precio);
        """)
        
        # Confirmar los cambios
        db.conn.commit()
        
        # Recuperar los índices de la tabla productos
        cur.execute("SELECT * FROM pg_indexes WHERE tablename = 'productos'")
        rows = cur.fetchall()
        
        # Crear la tabla para mostrar los índices
        table = Table(title="Índices de productos")
        
        # Añadir columnas a la tabla con los nombres de las claves del primer resultado
        for col in rows[0].keys():
            table.add_column(col)
        
        # Añadir las filas a la tabla
        for row in rows:
            table.add_row(*[str(v) for v in row.values()])
        
        # Mostrar la tabla en la consola
        console.print(table)
