package main

import (
	"fmt"
)

// Función principal
func main() {
	a := []int{1, 2, 3, 4, 5}
	b := []int{6, 7, 8, 9, 10}
	c := []int{}

	for i := 0; i < len(a); i++ {
		c = append(c, a[i]*b[i])
	}
	fmt.Println(c)

	// Llamada a la función mostrar_texto
	MostrarTexto()

	// Llamada a la función multiplicar
	Multiplicar()

	// Llamada a la función multiplicar con variables globales
	aGlobal := 5
	bGlobal := 8
	MultiplicarGlobal(aGlobal, bGlobal)

	// Llamada a la función validar_dato
	dato := ValidarDato(aGlobal)
	fmt.Println(dato)
}

// Función para mostrar texto
func MostrarTexto() {
	fmt.Println("hola")
}

// Función para multiplicar y mostrar el resultado
func Multiplicar() {
	a := 5
	b := 8
	fmt.Println(a * b)
}

// Función para multiplicar usando variables globales
func MultiplicarGlobal(a, b int) {
	fmt.Println(a * b)
}

// Función para validar un dato
func ValidarDato(a int) bool {
	if a == 5 {
		return true
	}
	return false
}
