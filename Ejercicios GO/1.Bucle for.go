package main

import "fmt" // Importamos el paquete 'fmt' para la entrada y salida de datos

func main() {
	// Definimos un slice llamado 'nombres' con los valores especificados
	// En Go, un slice es similar a un array dinámico, pero más flexible.
	nombres := []string{"Esteban", "Hans", "Jhon", "Juan Pablo"}

	// Usamos un bucle 'for' para recorrer el slice 'nombres'
	// 'range' es utilizado para iterar sobre los elementos del slice
	// En cada iteración, 'nombre' recibe el valor de cada elemento del slice.
	for _, nombre := range nombres {
		// Imprimimos cada valor de 'nombre' en la consola
		// 'fmt.Println()' imprime el texto seguido de un salto de línea
		fmt.Println(nombre) // Imprime el nombre de cada elemento en el slice
	}
}
