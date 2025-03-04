const prompt = require('prompt-sync')();//funcion que permite capturar entradas del usuario para ejecutar en node.js
let Voltaje = Number(prompt('Ingrese el valor del voltaje del circuito: '))
let Resistencia = Number(prompt('Ingrese el valor de la resistencia del circuito: '))
Intensidad = Voltaje/Resistencia //Intesidad entiendase por amperaje
console.log('Al conectar un resistor de: ',Resistencia,'ohm, a una fuente de: ',Voltaje,' V, El voltage circulara una corriente de',Intensidad,'amperios')
//Para ejecutar en terminar: node "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\10.Ley Ohm.js"