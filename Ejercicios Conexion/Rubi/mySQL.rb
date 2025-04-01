require 'mysql2'

begin
  # Establece la conexión con la base de datos en XAMPP
  client = Mysql2::Client.new(
    host: "localhost",        # Dirección del servidor de la base de datos (local)
    username: "root",         # Usuario de MySQL
    password: "",             # Contraseña (debe configurarse si tiene una)
    database: "ecommerce3066478" # Base de datos específica
  )

  puts client
  puts "✅ Conexión exitosa"
  puts "🔎 Tipo de objeto de conexión: #{client.class}" # Muestra el tipo de objeto de conexión

  # Ejecutar consulta SQL para listar bases de datos
  results = client.query("SHOW DATABASES;")

  # Iterar sobre los resultados e imprimirlos
  results.each do |row|
    puts row
  end

rescue Mysql2::Error => e
  puts "❌ Error al conectar con MySQL: #{e.message}"

ensure
  # Cerrar la conexión si se estableció correctamente
  client.close if client
  puts "⚠️ Conexión cerrada"
end
