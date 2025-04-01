import java.util.Scanner;

public class Ciclo_for {

    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        // Crear el scanner para leer datos
        Scanner scanner = new Scanner(System.in);

        // Solicitar el primer valor
        System.out.println("Ingrese el primer valor:");
        double a = scanner.nextDouble();

        // Solicitar el segundo valor
        System.out.println("Ingrese el segundo valor:");
        double c = scanner.nextDouble();

        // Bucle para calcular la potencia 5 veces
        for (int i = 0; i < 5; i++) {
            double valor = Math.pow(a, c); // Calcular la potencia
            System.out.println("La potencia de " + a + " sobre " + c + " es: " + valor);
        }

        // Cerrar el scanner
        scanner.close();
    }
}
