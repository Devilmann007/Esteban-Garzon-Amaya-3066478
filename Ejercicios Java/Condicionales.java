import java.util.Scanner;

public class Condicionales {
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        // Crear el scanner para leer datos
        Scanner scanner = new Scanner(System.in);
        
        // Pedir al usuario que seleccione una figura para calcular su área
        System.out.println("Seleccione la figura a calcular su área:");
        System.out.println("1 para rombo");
        System.out.println("2 para rectángulo");
        System.out.println("3 para cuadrado");
        System.out.println("4 para trapecio");
        
        // Leer la opción seleccionada
        int figura = scanner.nextInt();
        double area;

        // Ejecutar el cálculo de área según la figura seleccionada
        switch (figura) {
            case 1 -> {
                // Rombo
                System.out.print("Ingresa el valor de la diagonal mayor: ");
                double Dmayor = scanner.nextDouble();
                System.out.print("Ingresa el valor de la diagonal menor: ");
                double Dmenor = scanner.nextDouble();
                area = (Dmayor * Dmenor) / 2;
                System.out.println("El área del rombo es: " + area);
            }

            case 2 -> {
                // Rectángulo
                System.out.print("Ingresa el valor del largo del rectángulo: ");
                double largo = scanner.nextDouble();
                System.out.print("Ingresa el valor del ancho del rectángulo: ");
                double ancho = scanner.nextDouble();
                area = largo * ancho;
                System.out.println("El área del rectángulo es: " + area);
            }

            case 3 -> {
                // Cuadrado
                System.out.print("Ingresa el valor del lado del cuadrado: ");
                double lado = scanner.nextDouble();
                area = lado * lado;
                System.out.println("El área del cuadrado es: " + area);
            }

            case 4 -> {
                // Trapecio
                System.out.print("Ingresa el valor de la base mayor: ");
                double Bmayor = scanner.nextDouble();
                System.out.print("Ingresa el valor de la base menor: ");
                double Bmenor = scanner.nextDouble();
                System.out.print("Ingresa la altura del trapecio: ");
                double H = scanner.nextDouble();
                area = ((Bmayor + Bmenor) * H) / 2;
                System.out.println("El área del trapecio es: " + area);
            }

            default -> System.out.println("Opción no válida.");
        }

        // Cerrar el scanner al final
        scanner.close();
    }
}
