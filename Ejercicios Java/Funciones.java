public class Funciones {
    public static void main(String[] args) {
        // Parte 1: Definir arreglos y realizar la multiplicación
        int[] a = {1, 2, 3, 4, 5};
        int[] b = {6, 7, 8, 9, 10};
        int[] c = new int[a.length];

        // Bucle for para recorrer los índices de los arreglos a y b y multiplicarlos
        for (int i = 0; i < a.length; i++) {
            c[i] = a[i] * b[i];  // Almacena la multiplicación en el arreglo c
        }

        // Imprimir el arreglo c
        System.out.print("Resultado de multiplicaciones: ");
        for (int i = 0; i < c.length; i++) {
            System.out.print(c[i] + " ");
        }
        System.out.println();  // Salto de línea

        // Parte 2: Función que imprime un texto
        mostrarTexto();

        // Parte 3: Funciones de multiplicación
        multiplicacion1();

        // Parte 4: Función multiplicación con variables externas
        multiplicacion2();

        // Parte 5: Función que retorna un valor y lo suma
        int resultado = multiplicar();
        System.out.println("Resultado de la multiplicación más 5: " + (resultado + 5));

        // Parte 6: Validar si el valor de 'a' es igual a 5
        boolean dato = validarDato();
        System.out.println("El dato es válido: " + dato);
    }

    // Función que muestra un texto
    public static void mostrarTexto() {
        System.out.println("Hola mundo");
    }

    // Función multiplicación con variables dentro de la función
    public static void multiplicacion1() {
        int x = 5;
        int y = 8;
        System.out.println("Multiplicación dentro de la función: " + (x * y));
    }

    // Función multiplicación con variables fuera de la función
    public static void multiplicacion2() {
        int x = 5;
        int y = 8;
        System.out.println("Multiplicación con variables externas: " + (x * y));
    }

    // Función que retorna la multiplicación de dos números
    public static int multiplicar() {
        int a = 5;
        int b = 8;
        return a * b;
    }

    // Función que valida si la variable 'a' es igual a 5
    public static boolean validarDato() {
        int a = 5;
        return a == 5;
    }
}
