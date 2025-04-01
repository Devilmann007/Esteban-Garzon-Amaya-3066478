import java.util.Scanner;

public class Interaccion_Usuarios {
    public static void main(String[] args) {
        // Solicitar el nombre completo
        try ( // Crear un objeto Scanner para leer las entradas del usuario
                Scanner scanner = new Scanner(System.in)) {
            // Solicitar el nombre completo
            System.out.print("Escriba sus nombres completos: ");
            String a = scanner.nextLine();
            // Solicitar los apellidos completos
            System.out.print("Escriba sus Apellidos completos: ");
            String b = scanner.nextLine();
            // Solicitar la profesión
            System.out.print("Escriba su profesión: ");
            String c = scanner.nextLine();
            // Solicitar el año de nacimiento
            System.out.print("Escriba su año de nacimiento: ");
            int d = scanner.nextInt();
            // Calcular la edad
            int e = 2025 - d;
            // Mostrar el resultado
            System.out.println("El (La) " + c + " " + a + " " + b + " tiene " + e + " años");
            // Cerrar el scanner
        }
    }
}
