import java.util.Scanner;

public class Bucles_while {
    public static void main(String[] args) {
        // Parte 1: Contador con un bucle while
        int contador = 0;
        while (contador < 30) {
            contador += 1;
            System.out.println("Iteración " + contador);
        }

        // Parte 2: Combinado con un bucle while y un if-else
        try (Scanner scanner = new Scanner(System.in)) { // try-with-resources
            while (true) {
                System.out.println("Introduzca un valor mayor a 10:");
                int a = scanner.nextInt();  // Lee el valor ingresado por el usuario

                if (a > 10) {
                    System.out.println("Es correcto");
                    break;  // Sale del bucle cuando el valor ingresado es mayor que 10
                } else {
                    System.out.println("Es incorrecto, pruebe de nuevo");
                }
            }
        } catch (Exception e) {
            System.out.println("Ocurrió un error con la entrada: " + e.getMessage());
        }
    }
}


