<?php
require 'vendor/autoload.php'; // Cargar la librería de MongoDB

use MongoDB\Client;

try {
    // Conectar a MongoDB en localhost
    $cliente = new Client("mongodb://localhost:27017");

    // Mensaje de conexión exitosa
    echo "✅ Conexión exitosa a MongoDB<br>";

    // Listar bases de datos disponibles
    $basesDeDatos = $cliente->listDatabases();
    echo "📁 Bases de datos disponibles:<br>";
    foreach ($basesDeDatos as $db) {
        echo "- " . $db['name'] . "<br>";
    }

    // Seleccionar la base de datos y colección
    $mibasededatos = $cliente->ecommerce3066478;
    $micoleccion = $mibasededatos->Clientes1;

    // Nuevo documento a insertar
    $documento = [
        "Nombre" => "Laura Gómez",
        "Correo" => "laura.gomez@email.com",
        "Telefono" => "3107896543",
        "Direccion" => "Calle 45 #23-10",
        "Creado desde" => "PHP",
    ];

    // Insertar documento en la colección
    $resultado = $micoleccion->insertOne($documento);

    // Mostrar el ID del documento insertado
    echo "📌 Documento insertado con ID: " . $resultado->getInsertedId() . "<br>";

} catch (Exception $e) {
    echo "❌ Error: " . $e->getMessage();
} finally {
    echo "⚠️ Conexión cerrada";
}
?>
