public class Variables {
    public static void main(String[] args) {
        // Aplicando variables.
        int a = 10;
        int b = 4;
        int c;

        // Multiplicación:
        System.out.println("la primera variable es: " + a);
        System.out.println("el signo de la operación es: * ");
        System.out.println("la segunda variable es: " + b);
        c = a * b;
        System.out.println("el resultado es: " + c);
        System.out.println("Tipo de c: " + ((Object)c).getClass().getName()); // Tipo de c

        // División:
        System.out.println("la primera variable es: " + a);
        System.out.println("el signo de la operación es: / ");
        System.out.println("la segunda variable es: " + b);
        c = a / b;
        System.out.println("el resultado es: " + c);
        System.out.println("Tipo de c: " + ((Object)c).getClass().getName()); // Tipo de c

        // Suma:
        System.out.println("la primera variable es: " + a);
        System.out.println("el signo de la operación es: + ");
        System.out.println("la segunda variable es: " + b);
        c = a + b;
        System.out.println("el resultado es: " + c);
        System.out.println("Tipo de c: " + ((Object)c).getClass().getName()); // Tipo de c

        // Resta:
        System.out.println("la primera variable es: " + a);
        System.out.println("el signo de la operación es: - ");
        System.out.println("la segunda variable es: " + b);
        c = a - b;
        System.out.println("el resultado es: " + c);
        System.out.println("Tipo de c: " + ((Object)c).getClass().getName()); // Tipo de c

        // Potenciación:
        System.out.println("la primera variable es: " + a);
        System.out.println("el signo de la operación es: ** ");
        System.out.println("la segunda variable es: " + b);
        double result = Math.pow(a, b); // Para potencia usamos Math.pow
        System.out.println("el resultado es: " + result);
        System.out.println("Tipo de resultado: " + ((Object)result).getClass().getName()); // Tipo de result

        // Porcentaje:
        System.out.println("la primera variable es: " + a);
        System.out.println("el signo de la operación es: % ");
        System.out.println("la segunda variable es: " + b);
        c = a % b;
        System.out.println("el resultado es: " + c);
        System.out.println("Tipo de c: " + ((Object)c).getClass().getName()); // Tipo de c
    }
}
