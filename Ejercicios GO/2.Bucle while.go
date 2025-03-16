//Go no tiene una estructura while como en otros lenguajes, pero puedes lograr el mismo comportamiento con un bucle for.
package main

import (
    "fmt"
)

func main() {
    // Simulación de while usando for en Go
    contador := 0

    for contador < 30 { // Mientras contador < 30
        contador++
        fmt.Println("Iteración", contador) // Imprime la iteración
    }

    // Bucle infinito con entrada de usuario
    for {
        fmt.Println("Introduzca un valor mayor a 10:")

        var a int
        fmt.Scan(&a) // Lee un número entero desde la entrada

        if a > 10 {
            fmt.Println("Es correcto")
        } else {
            fmt.Println("Es incorrecto, pruebe de nuevo")
            break // Sale del bucle si el número es incorrecto
        }
    }
}
