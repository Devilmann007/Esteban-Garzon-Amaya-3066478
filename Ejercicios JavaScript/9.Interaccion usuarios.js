const prompt = require('prompt-sync')();//funcion que permite capturar entradas del usuario para ejecutar en node.js
let a = (prompt('Escriba sus nombres completos: '))
let b = (prompt('Escribas sus Apellidos completos: '))
let c = (prompt('Escriba su profesion: '))
let d = Number(prompt('Escriba su año de nacimiento: '))
let e = 2025-d
console.log('El (La)',c,a,b,'tiene',e,'años')
//Para ejecutar en terminal: node "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\9.Interaccion usuarios.js"