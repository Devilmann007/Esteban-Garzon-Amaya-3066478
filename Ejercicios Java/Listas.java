public class Listas {

    public static void main(String[] args) {
        // Crear el primer array con los días de la semana
        String[] lista1 = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"};
        System.out.println(lista1[4]);  // Trae el elemento en la posición 4: "Viernes"

        // Crear el segundo array con los días de la semana
        String[] lista2 = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"};
        for (String dia : lista2) {
            System.out.println(dia);  // Imprime toda la lista
        }

        // Crear el tercer array
        String[] lista3 = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"};
        System.out.println(lista3[0] + " " + lista3[3]);  // Imprime el dato en las posiciones 0 y 3: "Lunes" y "Jueves"

        // Crear un array con diferentes tipos de datos (simulando un array multidimensional)
        Object[] lista4 = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", 1, 2, 3, new Object[]{"Esteban", 0.2, 2.25, true}};
        
        // Acceso a elementos dentro de la lista 4
        System.out.println(lista4[0] + " " + lista4[4]);  // Imprime "Lunes" y "Viernes"
        Object[] subArray = (Object[]) lista4[9];  // Accedemos al sub-array en la posición 9
        System.out.println(subArray[0] + " " + subArray[3]);  // Imprime "Esteban" y "true"
    }
}
