#Importamos libreria pymongo
from pymongo import MongoClient

# Conectar con MongoDB.
client = MongoClient("mongodb://localhost:27017/")

# Selecciona Base de datos y coleccion
db = client["Sena"]

coleccion = db["Estudiantes"]

Estudiantes = list(coleccion.find())#Convertimos el cursor en una lista para poder recorrerla varias veces 

# Encuentra todos los estudiantes que tienen una nota mayor a 8.
Nota_mayor = [ Estudiante for Estudiante in Estudiantes if Estudiante ["Nota"] > 8]#Itera sobre cada estudiante

# Encuentra los estudiantes que tienen 20 años.

Mayor_20 = [Estudiante for Estudiante in Estudiantes if Estudiante["Edad"] > 20]

# Condicional For para imprimir solo estudiantes con nota mayor a 8 
print("\n📌 Estudiantes con nota mayor a 8: ")
for Estudiante in Nota_mayor:
    print(f"{Estudiante['Nombres']} {Estudiante['Apellidos']} - Nota: {Estudiante['Nota']}")

# Condicional For para imprimir solo estudiantes con edad mayor a 20
print("\n📌 Estudiantes mayores de 20: ") 
for Estudiante in Mayor_20:
    print(f"{Estudiante['Nombres']} {Estudiante['Apellidos']} - Edad: {Estudiante['Edad']}")

# Actualiza la nota de "Ana" a 9.5.
Filtro = {"Nombres": "Ana"} #Criterio de busqueda
Actulizar_nota ={"$set": {"Nota": 9.5}} # $set modifica la nota de Ana

# Actualiza la base de datos con el nuevo dato
Cambio_nota = coleccion.update_one (Filtro, Actulizar_nota)

# Imprimir dato actualizado
if Cambio_nota.modified_count > 0:
    nuevo_dato = coleccion.find_one(Filtro)
    print("\n"f"✅ Nota actualizada correctamente. La nueva nota de {nuevo_dato['Nombres']} es: {nuevo_dato['Nota']}")
    #En este caso para imprimir solo el dato actualizado debemos crear una variable y llamar la coleccion utilizando el criterio de busqueda
else:
    nuevo_dato = coleccion.find_one(Filtro)
    print("\n"f"La nota ya es: {nuevo_dato['Nota']}")

# Verificamos la informacion
ana = coleccion.find_one({"Nombres": "Ana"})
print("\n"f"{ana['Nombres']} - Nota: {ana['Nota']}")

# Incrementa la edad de todos los estudiantes en 1 año.
Incremento_edad = coleccion.update_many({}, {"$inc": {"Edad": 1}})# $inc operador de actualizacion que incrementa o decrementa
print("\nEdad incrementada en un año\n")
for Estudiante in Estudiantes:
    print(f"{Estudiante['Nombres']} - Edad: {Estudiante['Edad']}")

# Encuentra los estudiantes que tienen una nota entre 7 y 9 y tienen menos de 22 años.
Nota_Edad = [Estudiante for Estudiante in Estudiantes if 7 <= Estudiante["Nota"]<=9 and Estudiante["Edad"]<=22]
print("\n📌 Estudiantes que su nota se encuentra entre 7 y 9, ademas tienen menos de 22 años\n") 
for Estudiante in Nota_Edad:
    print(f"{Estudiante['Nombres']} {Estudiante['Apellidos']} - Edad: {Estudiante['Edad']} - Nota: {Estudiante['Nota']}")

# Calcula el promedio de las notas de todos los estudiantes.
Suma_notas = sum(Estudiante['Nota'] for Estudiante in Estudiantes) #Suma la nota de los estudiantes
Total_estudiantes = len(Estudiantes) #len devuelve la cantidad de elementos de una estructura de datos

promedio = Suma_notas / Total_estudiantes

print("\n"f"El promedio de las notas de todos los estudiantes es: {promedio:.2f} ") # .2f nos permite solo imprimir dos decimales 

# Agrupa los estudiantes por curso y calcula la nota promedio por curso.
# defaultdict es una variante del diccionario dict de Python que permite asignar un valor predeterminado a las claves cuando aún no existen.
from collections import defaultdict
# Creamos diccionario para agrupar estudiantes por curso
Cursos = defaultdict(list)

for Estudiante in Estudiantes:
    Cursos[Estudiante['Curso']].append(Estudiante['Nota']) # Agrupa estudiantes por curso y agrega el dato nota al diccionario cursos

print(f"\n📌 Promedio de notas por curso: ")
for Curso, Nota in Cursos.items():
    Promedio_cursos = sum(Nota) / len(Nota)
    print("\n"f"{Curso}: {Promedio_cursos}")

# Crea un índice en el campo curso y explica cómo mejora el rendimiento de las consultas.
# Crear indice
coleccion.create_index("Curso")
print("\n✅ Índice creado en el campo 'Curso'")

# Mejora el rendimiento ya que sin un indice MongoDB revisa cada documento de la coleccion.
# Un indice organiza los datos internamente, encontrando coincidencias mas rapido.

# Realiza una consulta que utilice el índice creado.
# Buscar estudiantes de un curso específico.
Busqueda = coleccion.find({"Curso": "Análisis y Desarrollo de Software"})

for estudiante in Busqueda:
    print("\n"f"{estudiante["Nombres"]} {estudiante["Apellidos"]}: {estudiante["Curso"]}")

# Elimina todos los estudiantes que tienen una nota menor a 6.
# delete.many elimina todos los elementos que cumplan con la condicion
Nota_menor = coleccion.delete_many({"Nota": {"$lt": 6}}) #$lt significa menor que

print("\n"f"✅ Se eliminaron {Nota_menor.deleted_count} estudiantes con nota menor a 6.")

# Imprimimos lista de estudiantes actualizada
Estudiantes = list(coleccion.find())

print("\n📌 Estudiantes restantes en la base de datos: \n")
for estudiante in Estudiantes:
    print(f"{estudiante['Nombres']} {estudiante['Apellidos']} - Nota: {estudiante['Nota']}")

#Crea una colección cursos donde cada documento contenga un arreglo de estudiantes inscritos.
coleccion_cursos =db["Cursos"]

#Definimos una lista de cursos con estudiantes inscritos
cursos = [
    {
        "Curso": "Análisis y Desarrollo de Software",
        "Estudiantes": [
            {"Nombres": "Esteban", "Apellidos": "Garzón Amaya", "Edad": 27, "Nota": 9.5},
            {"Nombres": "Carlos", "Apellidos": "Pérez Ramírez", "Edad": 22, "Nota": 5.8}
        ]
    },
    {
        "Curso": "Entrenamiento Deportivo",
        "Estudiantes": [
            {"Nombres": "Ana", "Apellidos": "Martínez López", "Edad": 19, "Nota": 8.7},
            {"Nombres": "Laura", "Apellidos": "Fernández Gómez", "Edad": 18, "Nota": 8.9}
        ]
    },
    {
        "Curso": "Producción Agropecuaria",
        "Estudiantes": [
            {"Nombres": "Miguel", "Apellidos": "Torres Jiménez", "Edad": 26, "Nota": 6.8}
        ]
    }
]
# Insertar los documentos en la colección "Cursos"
coleccion_cursos.insert_many(cursos)

print("\n✅ Colección 'Cursos' creada con estudiantes inscritos.")

# Encuentra todos los cursos en los que está inscrito un estudiante específico.
# Criterios de busqueda
Nom_Estu = "Esteban"
Ape_Estu = "Garzón Amaya"

Cursos_Estu = coleccion_cursos.find({
    "Estudiantes": {
        "$elemMatch": {"Nombres": Nom_Estu, "Apellidos": Ape_Estu}
    }
})
# Imprimir los cursos en los que está inscrito
print(f"\n📌 Cursos en los que está inscrito {Nom_Estu} {Ape_Estu}:")
for curso in Cursos_Estu:
    print("\n"f"📚 {curso['Curso']}")