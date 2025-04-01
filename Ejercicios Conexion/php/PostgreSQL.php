<?php
// Instalar paquetes
// Composer require ext-pgsql
// Composer require ext-pdo_pgsql

try {
    // Establece conexión con la base de datos PostgreSQL
    $conn = pg_connect("host=localhost port=5432 dbname=postgres user=postgres password=Psql2025");
    
    if (!$conn) {
        throw new Exception("No se pudo conectar a PostgreSQL.");
    }
    
    echo "✅ Conexion exitosa\n";
    
    // Listar todas las bases de datos disponibles
    $result = pg_query($conn, "SELECT datname FROM pg_database");
    
    if (!$result) {
        throw new Exception("Error al ejecutar la consulta.");
    }
    
    echo "Bases de datos disponibles:\n";
    while ($row = pg_fetch_assoc($result)) {
        echo $row['datname'] . "\n";
    }
    
} catch (Exception $e) {
    echo "\u274C Error al conectar a la base de datos: " . $e->getMessage() . "\n";
} finally {
    // Verificar si la conexión existe antes de cerrarla
    if (isset($conn) && $conn) {
        pg_close($conn);
        echo "❗ Conexion cerrada\n";

    }
}