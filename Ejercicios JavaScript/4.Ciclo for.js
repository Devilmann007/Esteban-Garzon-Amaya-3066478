const prompt = require('prompt-sync')();//funcion que permite ingresar datos tipo input para ejecutar en node.js
console.log("Ingrese el primer valor")
let a = Number(prompt())
console.log('ingrese el segundo valor: ')
let c = Number(prompt())
for ( let i = 0; i < 5;i++){
    let valor = a ** c;
    console.log('la potencia de',a,'sobre',c,'es:',valor);
}
// Para ejecutar en terminal: node "C:\Users\Esteban Amaya\OneDrive - SENA\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\4.Ciclo for.js"
