package main

import "fmt"

func main(){

	var figura string

	fmt.Println("selecione la figura a calcular su area:")
	fmt.Println("1 para rombo") 
	fmt.Println("2 para rectangulo")
	fmt.Println("3 para cuadrado") 
	fmt.Println("4 para trapecio")
	fmt.Scanln(&figura)

	const Pi = 3.1416 
	var Area float64

	switch figura {
	case "1":
		var Dmayor, Dmenor float64
		fmt.Println("Ingrese el valor de la diagonal mayor del rombo")
		fmt.Scanln(&Dmayor)
		fmt.Println("ingresa el valor de la diagonal menor del rombo: ")
  		fmt.Scanln(&Dmenor)
  		Area = (Dmayor*Dmenor)/2
  		fmt.Printf("El area del rombo es: %.2f", Area)
	
	case "2":
		var Largo, Ancho float64
		fmt.Println("ingresa el valor del largo del rectangulo: ") 
  		fmt.Scanln(&Largo)
  		fmt.Println("ingresa el valor del ancho del rectangulo: ") 
  		fmt.Scanln(&Ancho)
  		Area = (Largo*Ancho)
  		fmt.Printf("El area del rectangulo es: %.2f", Area) 

	case "3":
		var Lado float64
		fmt.Println("ingresa el valor del lado del cuadrado: ") 
  		fmt.Scanln(&Lado)
		Area = (Lado*Lado)
  		fmt.Printf("El area del cuadrado es: %.2f",Area)
		
	case "4":
		var Bmayor, Bmenor, h float64
		fmt.Println("ingresa el valor de la base mayor: ") 
  		fmt.Scanln(&Bmayor)
  		fmt.Println("ingresa el valor de la base menor: ") 
  		fmt.Scanln(&Bmenor)
  		fmt.Println("ingrese la altura del trapecio: ") 
  		fmt.Scanln(&h)
  		Area = ((Bmayor+Bmenor)*h)/2
  		fmt.Printf("El area del trapecio es: %.2f",Area) 	
	default:
		fmt.Println("Opción no válida. Por favor, elija una opción entre 1 y 4.")
	}
}