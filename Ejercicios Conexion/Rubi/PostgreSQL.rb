# Instalar la gema necesaria
# gem install pg

# Importamos la librería 'pg' para conectarnos a PostgreSQL
require 'pg'

begin
  # Establece conexión con la base de datos PostgreSQL
  conn = PG.connect(
    host: "localhost",    # Dirección del servidor de la base de datos (local)
    user: "postgres",     # Usuario de PostgreSQL (por defecto suele ser 'postgres')
    password: "Psql2025", # Contraseña del usuario
    dbname: "postgres",   # Conectarse a la base de datos 'postgres' por defecto
    port: 5432            # Puerto de PostgreSQL (por defecto 5432)
  )

  puts conn
  puts "✅ Conexión exitosa"
  puts "🔎 Tipo de objeto de conexión: #{conn.class}"

  # Crear un cursor (en Ruby usamos `exec` en lugar de `cursor`)
  # Listar todas las bases de datos disponibles
  result = conn.exec("SELECT datname FROM pg_database")

  puts "📂 Bases de datos disponibles:"
  result.each do |row|
    puts row["datname"]
  end

rescue PG::Error => e
  puts "❌ Error al conectar con PostgreSQL: #{e.message}"

ensure
  # Cerrar la conexión si existe
  if conn
    conn.close
    puts "⚠️ Conexión cerrada"
  end
end
