from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(db):
    # Mostrar el título del módulo
    console.print(Panel.fit("📊[bold cyan]Consultas y Agregaciones[/bold cyan] 📊"))
    
    with db.get_cursor() as cur:
        # Ejecutar consulta de agregación
        cur.execute("""
        SELECT categoria_id, COUNT(*) AS total, AVG(precio) AS promedio
        FROM productos
        GROUP BY categoria_id
        """)
        
        rows = cur.fetchall()
        
        # Crear la tabla para mostrar el resultado
        table = Table(title="Resumen por Categoría")
        
        # Añadir columnas a la tabla con los nombres de las claves del primer resultado
        for col in rows[0].keys():
            table.add_column(col)
        
        # Añadir las filas a la tabla
        for row in rows:
            table.add_row(*[str(v) for v in row.values()])
        
        # Mostrar la tabla en la consola
        console.print(table)
