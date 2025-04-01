import java.util.Scanner;

class Usuario {
    String nombre;
    int pin;
    double saldo;

    // Constructor
    public Usuario(String nombre, int pin, double saldo) {
        this.nombre = nombre;
        this.pin = pin;
        this.saldo = saldo;
    }
}

class Banco {
    Usuario[] usuarios;

    // Constructor
    public Banco(Usuario[] usuarios) {
        this.usuarios = usuarios;
    }

    // Método para autenticar al usuario
    public Usuario autenticar(String nombre, int pin) {
        for (Usuario usuario : usuarios) {
            if (usuario.nombre.equals(nombre)) {
                if (usuario.pin == pin) {
                    System.out.println("Estás logeado");
                    return usuario; // Retorna el usuario autenticado
                } else {
                    System.out.println("Pin o nombre incorrectos");
                    return null; // Retorna null si el pin es incorrecto
                }
            }
        }
        System.out.println("El usuario no existe");
        return null; // Retorna null si el usuario no existe
    }

    // Método para sacar dinero
    public void sacarDinero(Usuario usuario, double cantidad) {
        if (usuario.saldo < cantidad) {
            System.out.println("Saldo insuficiente");
        } else {
            usuario.saldo -= cantidad;
            System.out.println("El saldo disponible es: " + usuario.saldo);
        }
    }
}

public class Cajero {
    @SuppressWarnings("ConvertToStringSwitch")
    public static void main(String[] args) {
        // Crear usuarios
        Usuario alejandra = new Usuario("Alejandra", 9711, 450);
        Usuario esteban = new Usuario("Esteban", 9707, 500);
        Usuario andres = new Usuario("Andres", 2734, 980);

        // Crear banco con los usuarios
        Banco banco = new Banco(new Usuario[]{alejandra, esteban, andres});

        try (// Crear el scanner para leer datos
        Scanner scanner = new Scanner(System.in)) {
            String nombre;
            int pin;
            double saldo;
            String opcion;

            // Bucle principal
            while (true) {
                System.out.println("Bienvenido al Banco, por favor, identifíquese.");
                System.out.print("Introduzca el nombre: ");
                nombre = scanner.nextLine();
                System.out.print("Introduzca el pin: ");
                pin = scanner.nextInt();
                scanner.nextLine(); // Limpiar el buffer de la línea

                // Intentar autenticar
                Usuario usuario = banco.autenticar(nombre, pin);

                if (usuario != null) {
                    // Usuario autenticado, mostrar opciones
                    while (true) {
                        System.out.println("Por favor, elija una de estas opciones:");
                        System.out.println("1. Sacar dinero");
                        System.out.println("2. Terminar sesión");
                        System.out.print("Opción: ");
                        opcion = scanner.nextLine();

                        if (opcion.equals("1")) {
                            // Opción de sacar dinero
                            System.out.print("Introduce cantidad a sacar: ");
                            saldo = scanner.nextDouble();
                            scanner.nextLine(); // Limpiar el buffer de la línea
                            banco.sacarDinero(usuario, saldo);
                        } else if (opcion.equals("2")) {
                            // Terminar sesión
                            System.out.println("Saliendo del sistema.");
                            break;
                        } else {
                            System.out.println("Opción incorrecta. Por favor, introduzca otra opción.");
                        }
                    }
                } else {
                    System.out.println("Usuario no autenticado. Por favor, introduzca nombre y pin correctos.");
                }
            }
        }
    }
}
