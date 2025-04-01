#include <iostream>
#include <stdexcept>
#include <mysql_driver.h>
#include <mysql_connection.h>

using namespace std;

int main() {
    try {
        // Establecer conexión con la base de datos XAMPP
        sql::mysql::MySQL_Driver *driver;
        sql::Connection *conn;

        driver = sql::mysql::get_mysql_driver_instance();
        conn = driver->connect("tcp://127.0.0.1:3306", "root", "");  // Dirección, usuario y contraseña

        // Conectar a una base de datos específica
        conn->setSchema("ecommerce3066478");

        // Si la conexión se establece correctamente, imprimir un mensaje de éxito
        cout << "✅ Conexion exitosa" << endl;
        cout << "🔎 Tipo de objeto de conexión: " << typeid(conn).name() << endl;  // Muestra el tipo de objeto de conexión

        // Crear un puntero de tipo "Statement" para ejecutar comandos SQL
        sql::Statement *stmt = conn->createStatement();

        // Ejecutar una consulta SQL para listar las bases de datos en el servidor
        sql::ResultSet *res = stmt->executeQuery("SHOW DATABASES;");

        // Iterar sobre los resultados y imprimir las bases de datos
        while (res->next()) {
            cout << res->getString(1) << endl;  // Imprimir el nombre de cada base de datos
        }

        // Liberar recursos
        delete res;
        delete stmt;
        delete conn;

    } catch (sql::SQLException &e) {
        // Capturar cualquier error de conexión y mostrarlo
        cout << "❗ Error al conectar con MySQL: " << e.what() << endl;
    }

    return 0;
}
