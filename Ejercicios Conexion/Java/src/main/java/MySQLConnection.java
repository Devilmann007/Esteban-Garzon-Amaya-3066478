import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class MySQLConnection {
    public static void main(String[] args) {
        // Configuración de conexión a MySQL
        String url = "jdbc:mysql://localhost:3306/ecommerce3066478"; // URL de conexión con la base de datos
        String user = "root"; // Usuario de MySQL
        String password = ""; // Contraseña (dejar en blanco si no tiene)

        Connection conn = null;
        Statement stmt = null;

        try {
            // Establecer la conexión con la base de datos
            conn = DriverManager.getConnection(url, user, password);
            System.out.println("\u2705 Conexión exitosa a la base de datos");
            System.out.println("\u0001F50E Tipo de objeto de conexión: " + conn.getClass().getName());
            
            // Crear un objeto Statement para ejecutar consultas SQL
            stmt = conn.createStatement();
            
            // Ejecutar la consulta para obtener las bases de datos disponibles
            ResultSet rs = stmt.executeQuery("SHOW DATABASES;");
            
            // Iterar sobre los resultados e imprimirlos
            while (rs.next()) {
                System.out.println(rs.getString(1));
            }
            
            // Cerrar el ResultSet
            rs.close();
        } catch (SQLException e) {
            // Capturar errores de conexión o ejecución SQL
            System.out.println("\u274C Error al conectar con MySQL: " + e.getMessage());
        } finally {
            // Cerrar recursos
            try {
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
                System.out.println("\u2757 Conexión cerrada");
            } catch (SQLException e) {
                System.out.println("\u26A0 Error al cerrar la conexión: " + e.getMessage());
            }
        }
    }
}
