# Instalar la gema necesaria
# gem install mongo

# Importamos la librería mongo
require 'mongo'

begin
  # Conexión por localhost
  cliente = Mongo::Client.new(["localhost:27017"], database: "ecommerce3066478")

  # Si la conexión es exitosa
  puts cliente
  puts "✅ Conexión exitosa"

  # Imprime el tipo de objeto creado
  puts "🔎 Tipo de objeto de conexión: #{cliente.class}"

  # Listar todas las bases de datos disponibles en el servidor
  puts "📁 Bases de datos disponibles: #{cliente.database_names}"

  # Creamos o accedemos a la colección llamada "Clientes1" dentro de la base de datos
  micoleccion = cliente[:Clientes1]

  # Documento que se insertará en la colección (Datos modificados)
  documento = {
    "Nombre" => "Carlos Pérez",
    "Correo" => "carlos_perez@gmail.com",
    "telefono" => "3123456789",
    "Direccion" => "Av. Siempre Viva 742",
    "Creado desde" => "Rubi",
  }

  # Insertamos el documento en la colección
  resultado = micoleccion.insert_one(documento)

  # Imprimimos el ID del documento insertado
  puts "📌 Documento insertado con ID: #{resultado.inserted_id}"

rescue StandardError => e
  puts "❌ Error: #{e}"

ensure
  # Cerramos la conexión con el servidor
  cliente.close
  puts "⚠️ Conexión cerrada"
end
