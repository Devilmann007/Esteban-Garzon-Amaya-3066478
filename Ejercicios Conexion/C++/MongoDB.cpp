#include <iostream>
#include <mongocxx/client.hpp>
#include <mongocxx/instance.hpp>
#include <mongocxx/uri.hpp>
#include <bsoncxx/builder/stream/document.hpp>

int main() {
    // Iniciar MongoDB
    mongocxx::instance instancia{};

    try {
        // Conectar a MongoDB
        mongocxx::client cliente{mongocxx::uri{"mongodb://localhost:27017/"}};
        std::cout << "✅ Conexión exitosa a MongoDB" << std::endl;

        // Seleccionar la base de datos y la colección
        auto db = cliente["ecommerce3066478"];
        auto coleccion = db["Clientes1"];

        // Crear documento
        bsoncxx::builder::stream::document doc{};
        doc << "Nombre" << "Carlos Martínez"
            << "Correo" << "carlos.martinez@email.com"
            << "Telefono" << "3204567890"
            << "Direccion" << "Carrera 12 #34-56"
            << "Creado desde" << "C++";

        // Insertar documento
        auto resultado = coleccion.insert_one(doc.view());
        if (resultado) {
            std::cout << "📌 Documento insertado con ID: " 
                      << resultado->inserted_id().get_oid().value.to_string() 
                      << std::endl;
        }

    } catch (const std::exception& e) {
        std::cerr << "❌ Error: " << e.what() << std::endl;
    }

    return 0;
}

