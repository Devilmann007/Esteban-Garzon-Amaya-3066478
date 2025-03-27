// Instalar paquetes necesarios
// Ejecutar en la terminal: npm install mongodb

// Importamos la librería mongodb
const { MongoClient } = require('mongodb');

// URL de conexión a MongoDB
const url = "mongodb://localhost:27017/";

// Nombre de la base de datos
const dbName = "ecommerce3066478";

// Función principal para ejecutar la conexión y operaciones
async function main() {
    // Creamos una instancia del cliente MongoDB
    const client = new MongoClient(url);

    try {
        // Conectamos al servidor
        await client.connect();
        console.log("✅ Conexión exitosa");

        // Imprimimos el tipo de objeto creado
        console.log(`🔍 Tipo de objeto de conexión: ${client.constructor.name}`);

        // Listar todas las bases de datos disponibles en el servidor
        const databasesList = await client.db().admin().listDatabases();
        console.log("📁 Bases de datos disponibles: ", databasesList.databases.map(db => db.name));

        // Creamos o accedemos a la base de datos llamada "ecommerce3066478"
        const db = client.db(dbName);

        // Creamos o accedemos a la colección llamada "Clientes1" dentro de la base de datos
        const collection = db.collection("Clientes1");

        // Documento que se insertará en la colección
        const documento = {
            Nombre: "Bob", 
            Correo: "bob456@gmail.com",
            telefono: "3216549870",
            Direccion: "av 15 #45 - 67",
            "Creado desde": "JavaScript"
        };

        // Insertamos el documento en la colección
        const resultado = await collection.insertOne(documento);

        // Imprimimos el ID del documento insertado
        console.log(`📌 Documento insertado con ID: ${resultado.insertedId}`);

    } catch (err) {
        console.error("❌ Error:", err);
    } finally {
        // Cerramos la conexión con el servidor
        await client.close();
        console.log("❗ Conexión cerrada");
    }
}

// Ejecutamos la función principal
main().catch(console.error);
