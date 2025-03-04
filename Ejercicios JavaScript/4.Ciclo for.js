const prompt = require('prompt-sync')();//funcion que permite ingresar datos tipo input para ejecutar en node.js
console.log("Ingrese el primer valor")
a = Number(prompt())
b = 0
console.log('ingrese el segundo valor: ')
c = Number(prompt())
for ( let valor of Range(1)){
    valor=a**c
    console.log('la potencia de',a,'sobre',c,'es:',valor)
}