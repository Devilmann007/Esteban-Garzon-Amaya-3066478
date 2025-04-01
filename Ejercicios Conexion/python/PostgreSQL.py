#Instalar paquetes
#pip install psycopg2
#pip install psycopg2-binary
#pip install psycopg2-pool 
import psycopg2

try:
    #Establece conexion con la base de datos PostgreSQL
    conn = psycopg2.connect(  
        host="localhost",     #Direccion del servidor de la base de datos (en este caso, local)
        user="postgres",      #Usuario de PostgreSQL (por defecto suele ser 'postgres')
        password="Psql2025",  #Contraseña del usuario
        database="postgres",  #Concectarse a la base de datos 'postgres' por defecto 
        port=5432             #Puesto de posgreSQL(por defecto 5432)
    ) 

    print(conn)
    print("\u2705 Conexion exitosa")
    print(type(conn))

    #Crear un cursor para ejecutar consultas en la base de datos
    cursor=conn.cursor()

    #Listar todas las bases de datos disponibles
    cursor.execute("SELECT datname FROM pg_database")
    print("Bases de datos disponibles: ")
    for db in cursor:
        print(db)
    
    #Crear nueva base de datos
   

    # Captura errores de conexion y mostrarlos en pantalla
except Exception as e:
    print("\u274C Error al conectar a la base de datos:", e)
except psycopg2.Error as err:
    # Captura errores específicos de PostgreSQL y los muestra
    print(f"\u274C Error al conectar con PostgreSQL: {err}")
finally:
    # Verificar si el cursor existe antes de cerrarlo 
    if "cursor" in locals() and cursor:
        cursor.close()
        print(" \u2757 Cursor cerrado")

    # Verificar si la conexion existe antes de cerrarlo
    if "conn" in locals() and conn:
        conn.close()
        print(" \u2757 Conexion cerrada")