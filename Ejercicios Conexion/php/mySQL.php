<?php
// Datos de conexión
$host = "localhost";
$user = "root";
$password = "";
$database = "ecommerce3066478";

try {
    // Crear conexión
    $conn = new mysqli($host, $user, $password, $database);

    // Verificar conexión
    if ($conn->connect_error) {
        throw new Exception("❌ Error al conectar con MySQL: " . $conn->connect_error);
    }

    echo "✅ Conexión exitosa\n";
    echo "🔍 Tipo de objeto de conexión: " . get_class($conn) . "\n";

    // Ejecutar consulta SQL para listar bases de datos
    $result = $conn->query("SHOW DATABASES;");

    if ($result) {
        while ($row = $result->fetch_array()) {
            echo "📂 " . $row[0] . "\n";
        }
    } else {
        echo "⚠️ Error al obtener bases de datos: " . $conn->error;
    }
} catch (Exception $e) {
    echo $e->getMessage();
} finally {
    // Cerrar conexión si está abierta
    if (isset($conn) && $conn->ping()) {
        $conn->close();
        echo "❗ Conexión cerrada";
    }
}
?>
