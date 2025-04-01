import java.util.Scanner;

public class Ley_Ohm {
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        // Crear un objeto Scanner para leer las entradas del usuario
        Scanner scanner = new Scanner(System.in);

        // Solicitar el valor del voltaje
        System.out.print("Ingrese el valor del voltaje del circuito: ");
        double voltaje = scanner.nextDouble();

        // Solicitar el valor de la resistencia
        System.out.print("Ingrese el valor de la resistencia del circuito: ");
        double resistencia = scanner.nextDouble();

        // Calcular la intensidad (amperaje)
        double intensidad = voltaje / resistencia;

        // Mostrar el resultado
        System.out.println("Al conectar un resistor de: " + resistencia + " ohm, a una fuente de: " + voltaje + " V, El voltaje circulará una corriente de " + intensidad + " amperios.");

        // Cerrar el scanner
        scanner.close();
    }
}
