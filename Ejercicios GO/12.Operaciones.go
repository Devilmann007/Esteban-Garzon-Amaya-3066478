package main

import "fmt"

func main() {
	var A, B float64 // Declaramos las variables A y B como float64 para permitir números decimales.

	// Solicitar el primer valor al usuario
	fmt.Println("Ingrese valor para A: ")
	fmt.Scanln(&A) // Usamos &A para pasar la dirección de la variable.

	// Solicitar el segundo valor al usuario
	fmt.Println("Ingrese valor para B: ")
	fmt.Scanln(&B) // Usamos &B para pasar la dirección de la variable.

	// Realizar operaciones
	suma := A + B
	fmt.Println("La suma de los números es:", suma)

	res := A - B
	fmt.Println("La resta de los números es:", res)

	multi := A * B
	fmt.Println("La multiplicación de los números es:", multi)

	if B != 0 { // Verificamos que B no sea cero para evitar división por cero.
		div := A / B
		fmt.Println("La división de los números es:", div)
	} else {
		fmt.Println("No se puede dividir por cero.")
	}

	igual := A == B
	fmt.Println("Los números son iguales:", igual)

	// Comparar A y B
	if A > B {
		fmt.Println("El número menor es:", B)
		fmt.Println("El número mayor es:", A)
	} else if A < B {
		fmt.Println("El número menor es:", A)
		fmt.Println("El número mayor es:", B)
	} else {
		fmt.Println("Ambos números son iguales.")
	}
}
