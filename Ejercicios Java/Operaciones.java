import java.util.Scanner;

public class Operaciones{

    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        // Crear el scanner para leer datos
        Scanner scanner = new Scanner(System.in);

        // Solicitar al usuario que ingrese los valores
        System.out.print("Ingrese el primer valor: ");
        double A = scanner.nextDouble();

        System.out.print("Ingrese el segundo valor: ");
        double B = scanner.nextDouble();

        // Realizar las operaciones aritméticas
        double suma = A + B;
        System.out.println("La suma de los números es: " + suma);

        double resta = A - B;
        System.out.println("La resta de los números es: " + resta);

        double multiplicacion = A * B;
        System.out.println("La multiplicación de los números es: " + multiplicacion);

        double division = A / B;
        System.out.println("La división de los números es: " + division);

        // Comparar si A es igual a B
        boolean igual = (A == B);
        System.out.println("¿El número " + A + " es igual a " + B + "? " + igual);

        // Encontrar el número mayor y menor entre A y B
        double mayor = (A > B) ? A : B;
        double menor = (A < B) ? A : B;
        System.out.println("El número menor es: " + menor);
        System.out.println("El número mayor es: " + mayor);

        // Cerrar el scanner
        scanner.close();
    }
}
