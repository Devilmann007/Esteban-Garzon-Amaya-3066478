//Diccionario
package main

import "fmt"

func main(){
	// Crear un mapa usando inicialización literal
	coche := map[string]string{
		"Marca": "Ford",
		"Color": "Rojo",
		"Modelo": "Sedan",
		"Placa": "ROS227",
	}
	fmt.Println(coche)

	fmt.Println(coche["Color"])
	coche ["Color"] = "Verde"
	fmt.Println(coche["Color"])

	fmt.Println(coche["Marca"])
	coche["Marca"] = "Renault"
	fmt.Println(coche["Marca"])

	fmt.Println(coche)
}	
