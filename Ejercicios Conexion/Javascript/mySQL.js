// Instalar paquetes necesarios
// Ejecutar en la terminal: npm install mysql2

// Importamos la librería mysql2
const mysql = require('mysql2');

// Configuración de la conexión a la base de datos
const connection = mysql.createConnection({
    host: 'localhost',          // Dirección del servidor de la base de datos (en este caso, local)
    user: 'root',               // Usuario de MySQL
    password: '',               // Contraseña del usuario de MySQL (debe configurarse si tiene una)
    database: 'ecommerce3066478' // Conectar a una base de datos específica
});

// Intentamos establecer la conexión
connection.connect((err) => {
    if (err) {
        // Capturamos cualquier error de conexión y lo imprimimos
        console.error(`❌ Error al conectar con MySQL: ${err.message}`);
        return;
    }

    // Si la conexión se establece correctamente, imprimir un mensaje de éxito
    console.log("✅ Conexión exitosa");
    console.log(`🔍 Tipo de objeto de conexión: ${connection.constructor.name}`); // Muestra el tipo de objeto de conexión

    // Ejecutamos una consulta SQL para listar las bases de datos en el servidor
    connection.query("SHOW DATABASES;", (err, results) => {
        if (err) {
            console.error(`❌ Error al ejecutar la consulta: ${err.message}`);
            return;
        }

        // Iteramos sobre los resultados y los imprimimos
        console.log("📁 Bases de datos disponibles:");
        results.forEach(db => {
            console.log(db.Database); // Imprimimos el nombre de cada base de datos
        });

        // Cerramos la conexión
        connection.end((err) => {
            if (err) {
                console.error(`❌ Error al cerrar la conexión: ${err.message}`);
                return;
            }
            console.log("❗ Conexión cerrada");
        });
    });
});
