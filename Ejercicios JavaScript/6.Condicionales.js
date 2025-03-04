const prompt = require('prompt-sync')();//funcion que permite ingresar datos tipo input para ejecutar en node.js
let Figura=Number(prompt(`selecione la figura a calcular su area: \n\n 1 para rombo\n\n 2 para rectangulo \n\n 3 para cuadrado \n\n 4 para trapecio \n\n: `))
let pi=3.1416
switch (Figura){
    case 1:
        let Dmayor= Number(prompt('ingresa el valor de la diagonal mayor: '))
        let Dmenor= Number(prompt('ingresa el valor de la diagonal menor: '))
        Area=((Dmayor*Dmenor)/2)
        console.log('El area del rombo es: ',Area)        
        break;
    case 2:
        let Largo= Number(prompt('ingresa el valor del largo del rectangulo: '))
        let Ancho= Number(prompt('ingresa el valor del ancho del rectangulo: '))
        Area=Largo*Ancho
        console.log('El area del rectangulo es: ',Area)
        break;
    case 3:
        let Lado= Number(prompt('ingresa el valor del lado del cuadrado: '))
        Area=Lado*Lado
        console.log('El area del cuadrado es: ',Area)
        break;
    case 4:
        let Bmayor= Number(prompt('ingresa el valor de la base mayor: '))
        let Bmenor=Number(prompt('ingresa el valor de la base menor: '))
        H=Number(prompt('ingrese la altura del trapecio: '))
        Area=(((Bmayor+Bmenor)*H)/2)
        console.log('El area del trapecio es: ',Area)   
}
//Para ejecutar en terminar: node "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\6.Condicionales.js"