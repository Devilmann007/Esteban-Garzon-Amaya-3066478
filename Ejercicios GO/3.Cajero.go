package main

import (
	"fmt"
)

// Usuario representa un usuario del sistema bancario
type Usuario struct {
	nombre string  // Nombre del usuario
	pin    int     // PIN del usuario
	saldo  float64 // Saldo del usuario
}

// NuevoUsuario crea un nuevo Usuario
func NuevoUsuario(nombre string, pin int, saldo float64) *Usuario {
	return &Usuario{nombre: nombre, pin: pin, saldo: saldo} // Devuelve un puntero a un nuevo Usuario
}

// Banco representa el sistema bancario que gestiona múltiples usuarios
type Banco struct {
	usuarios []*Usuario // Lista de punteros a objetos Usuario
}

// NuevoBanco crea un nuevo Banco con una lista de usuarios
func NuevoBanco(usuarios []*Usuario) *Banco {
	return &Banco{usuarios: usuarios} // Devuelve un puntero a un nuevo Banco
}

// Autenticar verifica las credenciales del usuario
func (b *Banco) Autenticar(nombre string, pin int) *Usuario {
	for _, usuario := range b.usuarios { // Itera sobre la lista de usuarios
		if usuario.nombre == nombre { // Comprueba si el nombre coincide
			if usuario.pin == pin { // Comprueba si el PIN coincide
				fmt.Println("Estás logueado") // Mensaje de éxito
				return usuario // Devuelve el usuario autenticado
			}
			fmt.Println("PIN incorrecto") // Mensaje de error si el PIN es incorrecto
			return nil // Devuelve nil si la autenticación falla
		}
	}
	fmt.Println("El usuario no existe") // Mensaje si el usuario no se encuentra
	return nil // Devuelve nil si el usuario no existe
}

// SacarDinero permite al usuario retirar dinero de su saldo
func (b *Banco) SacarDinero(usuario *Usuario, cantidad float64) {
	if usuario.saldo < cantidad { // Verifica si el saldo es suficiente
		fmt.Println("Saldo insuficiente") // Mensaje de error si no hay suficiente saldo
	} else {
		usuario.saldo -= cantidad // Resta la cantidad del saldo
		fmt.Printf("El saldo disponible es: %.2f\n", usuario.saldo) // Muestra el saldo restante
	}
}

func main() {
	// Creación de usuarios
	ana := NuevoUsuario("Ana", 9872, 450)          // Crea un usuario llamado Ana
	pablo := NuevoUsuario("Pablo", 5555, 200)      // Crea un usuario llamado Pablo
	rodrigo := NuevoUsuario("Rodrigo", 2222, 900)  // Crea un usuario llamado Rodrigo

	// Inicialización del banco con los usuarios
	banco := NuevoBanco([]*Usuario{ana, pablo, rodrigo}) // Crea un objeto Banco con los usuarios

	for {
		fmt.Println("Bienvenido al Banco, por favor, identifíquese.")
		var nombre string
		var pin int
		fmt.Print("Introduzca el nombre: ")
		fmt.Scan(&nombre) // Solicita el nombre del usuario
		fmt.Print("Introduzca el PIN: ")
		fmt.Scan(&pin) // Solicita el PIN del usuario

		usuarioAutenticado := banco.Autenticar(nombre, pin) // Intenta autenticar al usuario
		if usuarioAutenticado != nil { // Si la autenticación es exitosa
			for {
				fmt.Println("Elija una opción:\n 1. Sacar dinero\n 2. Terminar sesión.")
				var opcion string
				fmt.Scan(&opcion) // Solicita la opción elegida por el usuario

				switch opcion {
				case "1": // Si elige sacar dinero
					var cantidad float64
					fmt.Print("Introduce la cantidad a sacar: ")
					fmt.Scan(&cantidad) // Solicita la cantidad a retirar
					banco.SacarDinero(usuarioAutenticado, cantidad) // Intenta retirar el dinero
				case "2": // Si elige terminar sesión
					fmt.Println("Saliendo del sistema.") // Mensaje de salida
					break // Sale del bucle de opciones
				default: // Si la opción no es válida
					fmt.Println("Opción incorrecta. Por favor, introduzca otra opción.") // Mensaje de error
				}
			}
		} else {
			fmt.Println("Usuario no autenticado. Por favor, introduzca nombre y PIN correctos.") // Mensaje si la autenticación falla
		}
	}
}
