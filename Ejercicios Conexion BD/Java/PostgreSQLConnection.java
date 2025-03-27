import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class PostgreSQLConnection {
    public static void main(String[] args) {
        // Configuración de conexión a PostgreSQL
        String url = "jdbc:postgresql://localhost:5432/postgres"; // URL de conexión con la base de datos
        String user = "postgres";  // Usuario de PostgreSQL
        String password = "Psql2025";  // Contraseña del usuario

        Connection conn = null;
        Statement stmt = null;

        try {
            // Establecer la conexión con la base de datos
            conn = DriverManager.getConnection(url, user, password);
            System.out.println("\u2705 Conexión exitosa a PostgreSQL");
            System.out.println("\u0001F50E Tipo de objeto de conexión: " + conn.getClass().getName());

            // Crear un objeto Statement para ejecutar consultas SQL
            stmt = conn.createStatement();

            // Ejecutar la consulta para obtener las bases de datos disponibles
            ResultSet rs = stmt.executeQuery("SELECT datname FROM pg_database");

            // Iterar sobre los resultados e imprimir los nombres de las bases de datos
            System.out.println("Bases de datos disponibles:");
            while (rs.next()) {
                System.out.println(rs.getString(1));
            }

            // Cerrar el ResultSet
            rs.close();

        } catch (SQLException e) {
            // Capturar errores de conexión o ejecución SQL
            System.out.println("\u274C Error al conectar con PostgreSQL: " + e.getMessage());
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
