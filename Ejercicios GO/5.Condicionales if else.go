package main

import "fmt" // Importamos fmt para entrada y salida de datos

func main() {
    // Declaramos una variable entera 'a' con el valor 2
    a := 2

    // Condición if-else para verificar el valor de 'a'
    if a == 2 {
        fmt.Println("a vale 2")
    } else {
        fmt.Println("a es diferente de 2")
    }

    // Declaramos variables para nombre, edad y país
    Nombre := "Esteban"
    Edad := 28
    Pais := "Colombia"

    // Evaluamos varias condiciones con if-else
    if Nombre == "Esteban" && Edad == 28 && Pais == "Colombia" {
        //fmt.Sprintf es una forma más elegante y flexible de formatear cadenas. Permite incluir variables en una cadena de formato
        fmt.Printf("Su nombre es %s, tiene %d años y es de %s\n", Nombre, Edad, Pais)
    } else if Nombre == "Esteban" && Edad != 28 {
        fmt.Println("Su nombre es Esteban y no tiene 28 años")
    } else if Nombre != "Esteban" && Edad == 28 {
        fmt.Println("Su nombre no es Esteban y tiene 28 años")
    } else {
        fmt.Println("No se llama Esteban ni tiene 28 años")
    }
}
