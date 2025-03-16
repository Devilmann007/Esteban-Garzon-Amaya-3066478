package main

import "fmt"

func main(){
	var Voltaje, Resistencia, Intensidad float64
	fmt.Println("Ingrese el valor del voltaje del circuito: ")
	fmt.Scanln(Voltaje)
	fmt.Println("Ingrese el valor de la resistencia del circuito: ")
	fmt.Scanln(Resistencia)
	Intensidad = (Voltaje/Resistencia)
	fmt.Printf("Al conectar un resistor de %.2f ohm, a una fuente de %.2f V el voltage circulara una corriente de %.2f amperios", Voltaje, Resistencia, Intensidad)
}	
