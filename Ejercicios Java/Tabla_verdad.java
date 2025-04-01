public class Tabla_verdad {
    public static void main(String[] args) {
        // Tabla de la verdad
        // El operador lógico && solo devuelve true si ambos valores son true.
        boolean a = true;
        boolean b = false;
        System.out.println(a && b); // El resultado será "false" porque b es igual a false.

        // Convertimos los números a enteros
        int numA = 2;
        int numB = 3;
        int numC = 4;
        int numD = 10;

        // El operador lógico && solo devuelve true si ambos valores son true.
        System.out.println(numA == numB && numC < numD); // false, porque numA no es igual a numB.

        // El operador lógico ! invierte el valor de la expresión booleana a la que se le aplica.
        // El resultado de la expresión b && c > d es false (porque 3 no es mayor que 10)
        System.out.println(!(numA == numB) == (numB > numD)); // false
    }
}
