package main

import (
	"fmt"
)

func main() {
	var a, b, c string
	var d int

	// Solicitar entrada del usuario
	fmt.Print("Escriba sus nombres completos: ")
	fmt.Scanln(&a)
	fmt.Print("Escriba sus apellidos completos: ")
	fmt.Scanln(&b)
	fmt.Print("Escriba su profesión: ")
	fmt.Scanln(&c)
	fmt.Print("Escriba su año de nacimiento: ")
	fmt.Scanln(&d)

	// Calcular la edad
	e := 2025 - d

	// Imprimir el resultado
	fmt.Printf("El (La) %s %s %s tiene %d años\n", c, a, b, e)
}
