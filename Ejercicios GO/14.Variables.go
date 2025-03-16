package main // Paquete principal.

import "fmt" // Importamos el paquete fmt para imprimir en consola.

func main() { // Función principal.
	a := 10 // Asignamos 10 a a.
	b := 4  // Asignamos 4 a b.

	// Multiplicación
	fmt.Println("La primera variable es:", a) // Imprimimos a.
	fmt.Println("El signo de la operación es: *") // Imprimimos el signo.
	fmt.Println("La segunda variable es:", b) // Imprimimos b.
	c := a * b // Multiplicamos a y b.
	fmt.Println("El resultado es:", c) // Imprimimos el resultado.
	fmt.Println("Tipo de c:", fmt.Sprintf("%T", c)) // Imprimimos el tipo de c.

	// División
	fmt.Println("La primera variable es:", a) // Imprimimos a.
	fmt.Println("El signo de la operación es: /") // Imprimimos el signo.
	fmt.Println("La segunda variable es:", b) // Imprimimos b.
	c = a / b // Dividimos a entre b.
	fmt.Println("El resultado es:", c) // Imprimimos el resultado.
	fmt.Println("Tipo de c:", fmt.Sprintf("%T", c)) // Imprimimos el tipo de c.

	// Suma
	fmt.Println("La primera variable es:", a) // Imprimimos a.
	fmt.Println("El signo de la operación es: +") // Imprimimos el signo.
	fmt.Println("La segunda variable es:", b) // Imprimimos b.
	c = a + b // Sumamos a y b.
	fmt.Println("El resultado es:", c) // Imprimimos el resultado.
	fmt.Println("Tipo de c:", fmt.Sprintf("%T", c)) // Imprimimos el tipo de c.

	// Resta
	fmt.Println("La primera variable es:", a) // Imprimimos a.
	fmt.Println("El signo de la operación es: -") // Imprimimos el signo.
	fmt.Println("La segunda variable es:", b) // Imprimimos b.
	c = a - b // Restamos b de a.
	fmt.Println("El resultado es:", c) // Imprimimos el resultado.
	fmt.Println("Tipo de c:", fmt.Sprintf("%T", c)) // Imprimimos el tipo de c.

	// Potenciación
	fmt.Println("La primera variable es:", a) // Imprimimos a.
	fmt.Println("El signo de la operación es: **") // Imprimimos el signo.
	fmt.Println("La segunda variable es:", b) // Imprimimos b.
	c = 1 // Inicializamos c para la potenciación.
	for i := 0; i < b; i++ { // Calculamos a^b.
		c *= a // Multiplicamos c por a, b veces.
	}
	fmt.Println("El resultado es:", c) // Imprimimos el resultado.
	fmt.Println("Tipo de c:", fmt.Sprintf("%T", c)) // Imprimimos el tipo de c.

	// Módulo
	fmt.Println("La primera variable es:", a) // Imprimimos a.
	fmt.Println("El signo de la operación es: %") // Imprimimos el signo.
	fmt.Println("La segunda variable es:", b) // Imprimimos b.
	c = a % b // Calculamos el módulo de a y b.
	fmt.Println("El resultado es:", c) // Imprimimos el resultado.
	fmt.Println("Tipo de c:", fmt.Sprintf("%T", c)) // Imprimimos el tipo de c.
}
