import com.mongodb.client.*;
import org.bson.Document;

public class MongoDB {
    public static void main(String[] args) {
        try (MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017")) {
            MongoDatabase database = mongoClient.getDatabase("ecommerce3066478");
            MongoCollection<Document> collection = database.getCollection("Clientes1");

            Document documento = new Document()
                    .append("Nombre", "Carlos")
                    .append("Correo", "carlos123@example.com")
                    .append("Telefono", "3012345678")
                    .append("Direccion", "Calle 10 #20-30")
                    .append("Creado_desde", "Java");

            collection.insertOne(documento);
            System.out.println("✅ Documento insertado con éxito.");
        } catch (Exception e) {
            System.out.println("❌ Error: " + e.getMessage());
        }
    }
}
