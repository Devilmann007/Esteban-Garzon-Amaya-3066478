package main

import "fmt"

func main() {
	// Definimos un slice de strings que contiene los días de la semana.
	Lista1 := []string{"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"}
	fmt.Println(Lista1[4]) // Imprime "Viernes".

	// Definimos otro slice de strings con los mismos días de la semana.
	Lista2 := []string{"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"}
	fmt.Println(Lista2) // Imprime la lista completa.

	// Definimos un tercer slice de strings y mostramos los primeros tres días.
	Lista3 := []string{"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"}
	fmt.Println(Lista3[0:3]) // Imprime ["Lunes", "Martes", "Miercoles"].

	// Creamos un slice que puede contener diferentes tipos de datos.
	Lista4 := []interface{}{
		"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", 1, 2, 3,
		[]interface{}{"Esteban", 0.2, 2.25, true}, // Último elemento es otro slice.
	}

	// Accedemos al décimo elemento de Lista4 y lo convertimos a un slice de interface{}.
	subLista := Lista4[9].([]interface{})
	fmt.Println(subLista[0:3]) // Imprime ["Esteban", 0.2, 2.25].

	// Imprimimos elementos de las listas de forma separada.
	fmt.Println(Lista1[4]) // Imprime "Viernes".
	fmt.Println(Lista2) // Imprime la lista completa.

	// Imprimimos el primer y cuarto elemento de Lista3.
	fmt.Print(Lista3[0], " ") // Imprime "Lunes" seguido de un espacio.
	fmt.Println(Lista3[3]) // Imprime "Jueves".

	// Imprimimos elementos de Lista4 y de la sublista.
	fmt.Print(Lista4[0], " ") // Imprime "Lunes".
	fmt.Print(Lista4[4], " ") // Imprime "Viernes".
	fmt.Print(subLista[0], " ") // Imprime "Esteban".
	fmt.Println(subLista[3]) // Imprime "true".
}
