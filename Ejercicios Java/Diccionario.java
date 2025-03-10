import java.util.HashMap;

public class Diccionario {
    public static void main(String[] args) {
        // Definimos un HashMap, que es una colección de pares clave:valor
        HashMap<String, String> coche = new HashMap<>();

        // Agregamos atributos al HashMap
        coche.put("marca", "Ford");
        coche.put("color", "rojo");
        coche.put("modelo", "sedan");
        coche.put("placa", "ROS227");

        // Imprime todos los atributos contenidos en "coche"
        System.out.println(coche);

        // Imprime el atributo "color"
        System.out.println(coche.get("color"));

        // Cambia el valor dentro del atributo "color"
        coche.put("color", "verde");

        // Imprime el nuevo valor
        System.out.println(coche.get("color"));

        // Cambia el valor dentro del atributo "marca"
        coche.put("marca", "Renault");

        // Imprime el nuevo valor
        System.out.println(coche.get("marca"));

        // Imprime todos los atributos contenidos en "coche" luego de cambios
        System.out.println(coche);
    }
}
