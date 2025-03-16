package main // Define el paquete principal del programa

import (
    "fmt"  // Importa el paquete fmt para entrada y salida de datos
    "math" // Importa el paquete math para operaciones matemáticas avanzadas
)

func main() {
    // Solicitar el primer valor al usuario
    fmt.Print("Ingrese el primer valor: ") // Muestra el mensaje sin salto de línea
    var A int // Declara una variable entera A para almacenar el primer número
    fmt.Scan(&A) // Captura la entrada del usuario y almacena el valor en A

    // Solicitar el segundo valor al usuario
    fmt.Print("Ingrese el segundo valor: ") // Muestra el mensaje sin salto de línea
    var C int // Declara una variable entera C para almacenar el segundo número
    fmt.Scan(&C) // Captura la entrada del usuario y almacena el valor en C

    // Calcular la potencia de A elevado a C
    potencia := math.Pow(float64(A), float64(C)) 
    // math.Pow() requiere valores float64, por lo que convertimos A y C a float64
    // Guardamos el resultado en la variable potencia (de tipo float64)

    // Mostrar el resultado de la potencia
    fmt.Printf("La potencia de %d sobre %d es: %.0f\n", A, C, potencia)
    // %d se usa para enteros (A y C)
    // %.0f se usa para mostrar la potencia sin decimales
    // \n agrega un salto de línea después del mensaje
}
