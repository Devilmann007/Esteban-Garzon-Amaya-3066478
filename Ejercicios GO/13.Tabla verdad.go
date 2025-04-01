package main // Declaramos el paquete principal.

import "fmt" // Importamos el paquete fmt para imprimir en consola.

func main() { // Función principal donde comienza la ejecución del programa.

	// Primera parte: Evaluación de valores booleanos
	x := true  // Asignamos true a la variable x.
	y := false // Asignamos false a la variable y.
	
	// Imprimimos el resultado de la operación AND entre x e y.
	// La salida será false porque y es false.
	fmt.Println(x && y) // Imprime: false.

	// Segunda parte: Comparación de números
	a := 2 // Asignamos 2 a a.
	b := 2 // Asignamos 2 a b.
	c := 4 // Asignamos 4 a c.
	d := 10 // Asignamos 10 a d.
	
	// Imprimimos el resultado de dos comparaciones unidas por AND.
	// Ambas comparaciones son true, por lo que la salida es true.
	fmt.Println(a == b && c < d) // Imprime: true.

	// Tercera parte: Evaluación de expresiones
	// Imprimimos el resultado de una expresión con NOT y una comparación.
	// La primera parte es true, pero se invierte a false con NOT.
	// La segunda parte es false, así que la salida total es false.
	fmt.Println(!(a == b) && c > d) // Imprime: false.
}
