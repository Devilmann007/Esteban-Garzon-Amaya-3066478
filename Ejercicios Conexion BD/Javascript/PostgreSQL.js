// Instalar paquetes necesarios
// Ejecutar en la terminal: npm install pg

// Importamos la librería pg
const { Client } = require('pg');

// Configuración de la conexión a la base de datos
const client = new Client({
    host: 'localhost',          // Dirección del servidor de la base de datos (en este caso, local)
    user: 'postgres',           // Usuario de PostgreSQL (por defecto suele ser 'postgres')
    password: 'Psql2025',      // Contraseña del usuario
    database: 'postgres',       // Conectarse a la base de datos 'postgres' por defecto
    port: 5432                  // Puerto de PostgreSQL (por defecto 5432)
});

// Intentamos establecer la conexión
client.connect()
    .then(() => {
        console.log("✅ Conexión exitosa");
        console.log(`🔍 Tipo de objeto de conexión: ${client.constructor.name}`); // Muestra el tipo de objeto de conexión

        // Listar todas las bases de datos disponibles
        return client.query("SELECT datname FROM pg_database");
    })
    .then((res) => {
        console.log("📁 Bases de datos disponibles:");
        res.rows.forEach(db => {
            console.log(db.datname); // Imprimimos el nombre de cada base de datos
        });
    })
    .catch(err => {
        console.error("❌ Error al conectar a la base de datos:", err);
    })
    .finally(() => {
        // Cerramos la conexión
        client.end()
            .then(() => {
                console.log("❗ Conexión cerrada");
            })
            .catch(err => {
                console.error("❌ Error al cerrar la conexión:", err);
            });
    });
