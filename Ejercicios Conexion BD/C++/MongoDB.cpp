#include <iostream>
#include <mongocxx/client.hpp>
#include <mongocxx/instance.hpp>
#include <mongocxx/uri.hpp>
#include <bsoncxx/builder/stream/document.hpp>
#include <bsoncxx/json.hpp>

int main() {
    // Inicializar la instancia de MongoDB
    mongocxx::instance inst{};

    try {
        // Conectar al servidor local de MongoDB
        mongocxx::client cliente{mongocxx::uri{"mongodb://localhost:27017/"}};
        std::cout << "\u2705 Conexion exitosa" << std::endl;

        // Tipo de objeto de conexión
        std::cout << "\U0001F50E Tipo de objeto de conexión: " << typeid(cliente).name() << std::endl;

        // Listar bases de datos disponibles
        auto databases = cliente.list_databases();
        std::cout << "\U0001F4C1 Bases de datos disponibles: ";
        for (auto&& db : databases) {
            std::cout << db["name"].get_utf8().value << " ";
        }
        std::cout << std::endl;

        // Acceder o crear la base de datos "mydatabase"
        auto mibasededatos = cliente["mydatabase"];

        // Acceder o crear la colección "mycollection"
        auto micoleccion = mibasededatos["mycollection"];

        // Crear documento
        bsoncxx::builder::stream::document documento{};
        documento << "Nombre" << "Alice"
                  << "Edad" << 25
                  << "Ciudad" << "Wonderland";  // Nota: "Cuidad" estaba mal escrito en Python

        // Insertar documento en la colección
        auto resultado = micoleccion.insert_one(documento.view());
        if (resultado) {
            std::cout << "\U0001F4CC Documento insertado con ID: "
                      << resultado->inserted_id().get_oid().value.to_string()
                      << std::endl;
        }

    } catch (const std::exception& e) {
        std::cerr << "\u274C Error: " << e.what() << std::endl;
    }

    // Cerrar conexión (en C++ no es obligatorio, pero lo indicamos)
    std::cout << " \u2757 Conexion cerrada" << std::endl;
    return 0;
}
