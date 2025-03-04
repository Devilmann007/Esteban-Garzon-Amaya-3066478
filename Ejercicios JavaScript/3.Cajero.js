class Usuario {
    constructor(nombre, pin, saldo) { 
        this.nombre = nombre;
        this.pin = pin;
        this.saldo = saldo;
    }
}

class Banco {
    constructor(Usuarios = []) {
        this.Usuarios = Usuarios; // Guarda la lista de usuarios
    }

    autenticar(nombre, pin) { 
        // Busca el usuario por nombre y lo autentica si el pin es correcto
        for (let usuario of this.Usuarios) {
            if (usuario.nombre === nombre) {
                if (usuario.pin === pin) {
                    console.log("Estás logeado");
                    return usuario; // Retorna el usuario autenticado
                } else {
                    console.log("Pin o nombre incorrectos");
                    return null; // Retorna null si el pin es incorrecto
                }
            }
        }
        console.log("El usuario no existe");
        return null; // Retorna null si el usuario no existe
    }

    sacar_dinero(usuario, cantidad) { 
        // Se pasa el usuario autenticado y la cantidad a sacar
        if (usuario.saldo < cantidad) {
            console.log("Saldo insuficiente");
        } else {
            usuario.saldo -= cantidad;
            console.log(`El saldo disponible es ${usuario.saldo}`);//usar (`)
        }
    }
}

let alejandra = new Usuario("Alejandra", 9711, 450);
let esteban = new Usuario("Esteban", 9707, 500);
let andres = new Usuario("Andres", 2734, 980);

const prompt = require('prompt-sync')();
let banco = new Banco([alejandra, esteban, andres]);

let nombre, pin, saldo, opcion;
while (true) {
    console.log("Bienvenido al Banco, por favor, identifíquese.");
    console.log("Introduzca el nombre.");
    nombre = prompt();
    console.log("Introduzca el pin");
    pin = Number(prompt());

    let usuario = banco.autenticar(nombre, pin); // Aquí obtenemos el objeto de usuario

    if (usuario) {
        while (true) {
            console.log("Por favor, elija una de estas opciones:\n 1. Sacar dinero\n 2. Terminar sesión.");
            opcion = prompt();

            if (opcion === "1") {
                console.log("Introduce cantidad a sacar.");
                saldo = Number(prompt());
                banco.sacar_dinero(usuario, saldo);
            } else if (opcion === "2") {
                console.log("Saliendo del sistema.");
                break;
            } else {
                console.log("Opción incorrecta. Por favor, introduzca otra opción.");
            }
        }
    } else {
        console.log("Usuario no autenticado. Por favor, introduzca nombre y pin correctos.");
    }
}
// Para ejecutar en terminal: node "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\3.Cajero.js"
