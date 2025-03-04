//funcion que permite capturar entradas del usuario para ejecutar en node.js
const prompt = require('prompt-sync')();
//En este caso se le pedira al usuario el dato de entrada definidos en dos variables.
let A = Number(prompt('ingrese valor:'))//Number: define el valor de la variable como un numero.
let B = Number(prompt('ingrese valor:'))
//Definimos las operaciones a realizar.
let suma = A+B
console.log('la suma de los numeros es: ',suma)
let res = A-B
console.log('la resta de los numeros es: ',res)
let multi = A*B
console.log('la multiplicacion de los numeros es: ',multi)
let div = A/B 
console.log('la division de los numeros es: ',div)

//Definimos una variable que compare el igual y el mayor entre A y B.
let igual = A == B
console.log('el numero', A, 'es igual a',B,'?',igual)//Genera un valor booleano para comparar A y B.

let mayor = (A>B) ? A : B //Devuelve el valor numerico si el valor es verdadero.
let menor = (A<B) ? A : B //Devuelve el valor numerico si el valor es falso.
console.log('el numero menor es: ',menor)
console.log('el numero mayor es: ',mayor)
//Para ejecutar en terminar: node "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\12.Operaciones.js"