from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(db):
    # Mostrar el título del módulo
    console.print(Panel.fit("📈[bold cyan]Estadísticas del Sistema[/bold cyan] 📈"))
    
    with db.get_cursor() as cur:
        # Ejecutar la consulta para obtener las estadísticas del sistema
        cur.execute("""
        SELECT current_database() AS base, pg_size_pretty(pg_database_size(current_database())) AS tamaño;
        """)

        row = cur.fetchone()  # Recuperar solo una fila del resultado
        
        # Crear la tabla para mostrar las estadísticas
        table = Table(title="Uso de Base de Datos")
        
        # Añadir las columnas solo una vez, antes de iterar sobre los datos
        table.add_column("Métrica")
        table.add_column("Valor")
        
        # Añadir las filas a la tabla
        for k, v in row.items():
            table.add_row(k, v)
        
        # Imprimir la tabla con la información de uso de la base de datos
        console.print(table)
