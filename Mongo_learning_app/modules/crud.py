from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from bson.objectid import ObjectId

console = Console()

def run(db):
    """Módulo de operaciones CRUD"""
    console.print(Panel.fit("📝 [bold cyan]Operaciones CRUD en MongoDB[/bold cyan] 📝"))

    # Seleccionar colección
    collections = db.list_collection_names()
    if not collections:
        console.print("\ni️ No hay colecciones en esta base de datos. Creando una nueva...")
        collection_name = "ejemplo_crud"
        db.create_collection(collection_name)
    else:
        collection_name = console.input(f"\nIngrese el nombre de la colección ({', '.join(collections)}): ")

    collection = db[collection_name]

    while True:
        # Mostrar submenú CRUD
        table = Table(title="Operaciones CRUD", show_header=True)
        table.add_column("Opción", style="cyan")
        table.add_column("Operación", style="green")
        table.add_column("Descripción", style="white")

        table.add_row("1", "Insertar", "Agregar nuevos documentos")
        table.add_row("2", "Buscar", "Consultar documentos")
        table.add_row("3", "Actualizar", "Modificar documentos")
        table.add_row("4", "Eliminar", "Borrar documentos")
        table.add_row("5", "Conteo", "Contar documentos")
        table.add_row("0", "Volver","Regresar al menú principal")

        console.print(table)

        choice = console.input("\n🔹Seleccione una operación CRUD (0-5): ")

        if choice == "0":
            break

        elif choice == "1":
            # Insertar documentos
            console.print("\n[bold]Insertar documentos[/bold]")
            console.print("1. Insertar uno\n2. Insertar varios")
            insert_choice = console.input("Seleccione opción (1-2): ")

            if insert_choice == "1":
                doc = {}
                while True:
                    key = console.input("Ingrese clave (o dejar vacío para terminar): ")
                    if not key:
                        break
                    value = console.input(f"Ingrese valor para '{key}': ")
                    doc[key] = try_eval(value)

                if doc:
                    result = collection.insert_one(doc)
                    console.print(f"\n✅[green]Documento insertado con ID: {result.inserted_id}[/green]")
                else:
                    console.print("\n❌[red]No se proporcionaron datos para insertar[/red]")

            elif insert_choice == "2":
                docs = []
                console.print("\nIngrese documentos (deje 'id' vacío para terminar):")
                while True:
                    doc = {}
                    console.print(f"\nDocumento #{len(docs) + 1}:")
                    while True:
                        key = console.input("Ingrese clave (o dejar vacío para terminar documento): ")
                        if not key:
                            break
                        value = console.input(f"Ingrese valor para '{key}': ")
                        doc[key] = try_eval(value)

                    if doc:
                        docs.append(doc)
                    else:
                        break

                if docs:
                    result = collection.insert_many(docs)
                    console.print(f"\n✅[green]Insertados {len(result.inserted_ids)} documentos[/green]")
                    console.print(f"IDs: {result.inserted_ids}")
                else:
                    console.print("\n❌[red]No se proporcionaron documentos para insertar[/red]")

        elif choice == "2":
            # Buscar documentos
            console.print("\n[bold]Buscar documentos[/bold]")
            console.print("1. Buscar todos\n2. Buscar con filtro\n3. Buscar uno")
            find_choice = console.input("Seleccione opción (1-3): ")

            if find_choice == "1":
                docs = list(collection.find())
                print_documents(docs)

            elif find_choice == "2":
                try:
                    query = console.input("Ingrese filtro (ej: {'nombre': 'Juan'}): ")
                    query = eval(query) if query else {}
                    docs = list(collection.find(query))
                    print_documents(docs)

                except Exception as e:
                    console.print(f"\n❌[red]Error en la consulta: {e}[/red]")

            elif find_choice == "3":
                try:
                    query = console.input("Ingrese filtro (ej: {'_id': ObjectId('...')}): ")
                    query = eval(query) if query else {}
                    doc = collection.find_one(query)
                    if doc:
                        print_documents([doc])
                    else:
                        console.print("\ni️ No se encontraron documentos")
                except Exception as e:
                    console.print(f"\n❌[red]Error en la consulta: {e}[/red]")

        elif choice == "3":
            # Actualizar documentos
            console.print("\n[bold]Actualizar documentos[/bold]")
            console.print("1. Actualizar uno\n2. Actualizar varios")
            update_choice = console.input("Seleccione opción (1-2): ")

            try:
                filter_query = console.input("Ingrese filtro para seleccionar documentos (ej: {'nombre': 'Juan'}): ")
                filter_query = eval(filter_query) if filter_query else {}

                update_fields = console.input("Ingrese campos a actualizar (ej: {'edad': 30}): ")
                update_fields = eval(update_fields) if update_fields else {}

                if update_choice == "1":
                    result = collection.update_one(filter_query, {"$set": update_fields})
                    console.print(f"\n✅ [green]{result.modified_count} documento actualizado[/green]")
                
                elif update_choice == "2":
                    result = collection.update_many(filter_query, {"$set": update_fields})
                    console.print(f"\n✅ [green]{result.modified_count} documentos actualizados[/green]")

            except Exception as e:
                console.print(f"\n❌ [red]Error al actualizar: {e}[/red]")

        elif choice == "4":
            # Eliminar documentos
            console.print("\n[bold]Eliminar documentos[/bold]")
            console.print("1. Eliminar uno\n2. Eliminar varios")
            delete_choice = console.input("Seleccione opción (1-2): ")

            try:
                delete_query = console.input("Ingrese filtro para eliminar documentos (ej: {'nombre': 'Juan'}): ")
                delete_query = eval(delete_query) if delete_query else {}

                if delete_choice == "1":
                    result = collection.delete_one(delete_query)
                    console.print(f"\n✅ [green]{result.deleted_count} documento eliminado[/green]")

                elif delete_choice == "2":
                    result = collection.delete_many(delete_query)
                    console.print(f"\n✅ [green]{result.deleted_count} documentos eliminados[/green]")

            except Exception as e:
                console.print(f"\n❌ [red]Error al eliminar: {e}[/red]")

        elif choice == "5":
            # Contar documentos
            console.print("\n[bold]Conteo de documentos[/bold]")

            try:
                count_filter = console.input("Ingrese filtro para contar (opcional, ej: {'edad': 30}): ")
                count_filter = eval(count_filter) if count_filter else {}

                count = collection.count_documents(count_filter)
                console.print(f"\n🔢 [green]Total de documentos encontrados: {count}[/green]")

            except Exception as e:
                console.print(f"\n❌ [red]Error en el conteo: {e}[/red]")

        else:
            console.print("\n❌[red]Opción inválida. Intente nuevamente.[/red]")

        console.input("\nPresione Enter para continuar...")
        console.clear()

def try_eval(value):
    """Intenta evaluar el input como expresión Python, sino lo deja como string"""
    try:
        return eval(value)
    except:
        return value
    
def print_documents(docs):
    """Muestra documentos en una tabla formateada"""
    if not docs:
        console.print("\ni️ No se encontraron documentos")
        return
    
    # Crear tabla con las claves del primer documento
    table = Table(title="Documentos Encontrados", show_header=True)
    for key in docs[0].keys():
        table.add_column(str(key))

    for doc in docs:
        row = []
        for val in doc.values():
            if isinstance(val, ObjectId):
                row.append(str(val))
            else:
                row.append(str(val))
            table.add_row(*row)
        
    console.print(table)        