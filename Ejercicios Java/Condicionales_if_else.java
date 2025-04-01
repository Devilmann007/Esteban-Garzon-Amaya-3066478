public class Condicionales_if_else {
    public static void main(String[] args) {
        // Primer bloque de condiciones
        int a = 2;
        if (a == 2) {
            System.out.println("a vale 2");
        } else {
            System.out.println("a es diferente de 2");
        }

        // Concatenación de condiciones
        String nombre = "Esteban";
        int edad = 27;
        String pais = "Colombia";

        if (nombre.equals("Esteban") && edad == 27 && pais.equals("Colombia")) {
            System.out.println("Su nombre es " + nombre + ", tiene " + edad + " años y es de " + pais);
        } else if (nombre.equals("Esteban") && !(edad == 27)) { // && ! significa "Y no"
            System.out.println("Su nombre es Esteban y no tiene 27 años");
        } else if (!(nombre.equals("Esteban")) && (edad == 27)) {
            System.out.println("Su nombre no es Esteban y tiene 27 años");
        } else {
            System.out.println("No se llama Esteban ni tiene 27 años");
        }
    }
}
