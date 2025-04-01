//Tabla de la verdad
//El operador logico && solo devuelve true si ambos valores son true.
let a = true
let b = false
console.log(a && b)
//En este caso el resultado sera "false" por que b es igual a false 

a = Number(2)
b = Number(3)
c = Number(4)
d = Number(10)

//El operador logico && solo devuelve true si ambos valores son true.
console.log( a == b && c < d )
//El operador logico ! Invierte el valor de la expresión booleana a la que se le aplica.
console.log( ! a ==  (b && c > d) )
//Para ejecutar en terminal: node "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\13.Tabla de la verdad.js"