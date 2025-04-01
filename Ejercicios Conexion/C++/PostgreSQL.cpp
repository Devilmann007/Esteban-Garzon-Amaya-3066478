#include <iostream>
#include <pqxx/pqxx>  // Incluir la biblioteca libpqxx para PostgreSQL

using namespace std;

int main() {
    try {
        // Establece la conexión con la base de datos PostgreSQL
        string conn_info = "dbname=postgres user=postgres password=Psql2025 host=localhost port=5432";

        pqxx::connection conn(conn_info);

        if (conn.is_open()) {
            cout << "✅ Conexion exitosa" << endl;
            cout << "🔎 Tipo de objeto de conexión: " << typeid(conn).name() << endl;
        }

        // Crear un objeto "work" para ejecutar consultas SQL
        pqxx::work W(conn);

        // Ejecutar una consulta para listar todas las bases de datos
        pqxx::result R = W.exec("SELECT datname FROM pg_database");

        cout << "Bases de datos disponibles: " << endl;

        // Iterar sobre los resultados y mostrarlos
        for (auto row : R) {
            cout << row["datname"].c_str() << endl;
        }

        // Realizar cualquier otra acción (si es necesario)

        // Confirmar la transacción (aunque no es necesaria para SELECT)
        W.commit();

    } catch (const exception &e) {
        // Capturar cualquier error de conexión y mostrarlo
        cout << "❌ Error al conectar a la base de datos: " << e.what() << endl;
    }

    return 0;
}

